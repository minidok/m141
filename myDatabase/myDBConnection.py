#!/usr/bin/python
# Datenbank Verbindung mit postgres DB aufbauen
## Beschreibung Modul https://www.psycopg.org/psycopg3/docs/basic/usage.html
## Psycopg 3 – PostgreSQL database adapter for Python
import psycopg
import os
import logging
from config import config

# Configure logging for security monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def connect(section='postgresql_test'):
    """ Connect to the PostgreSQL database server with enhanced security """
    conn = None
    try:
        # Load configuration
        params = config(section=section)
        
        # Log connection attempt (without sensitive data)
        safe_params = {k: v for k, v in params.items() if k != 'password'}
        logger.info(f'Attempting to connect to database with params: {safe_params}')

        # Establish connection to PostgreSQL server with connection timeout
        print('Connecting to the PostgreSQL database...')
        conn = psycopg.connect(**params, connect_timeout=10)
        
        # Set connection to read-only mode for safety (remove for write operations)
        # conn.read_only = True
        
        # Get cursor for database operations
        cur = conn.cursor()
        
        # Execute query to verify connection
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Fetch query result
        db_version = cur.fetchone()
        print(db_version)
        
        logger.info('Database connection successful')
        
        # Close cursor
        cur.close()
        
    except psycopg.OperationalError as e:
        logger.error(f'Database connection failed: {e}')
        print(f'Connection error: {e}')
    except psycopg.DatabaseError as e:
        logger.error(f'Database error: {e}')
        print(f'Database error: {e}')
    except Exception as e:
        logger.error(f'Unexpected error: {e}')
        print(f'Unexpected error: {e}')
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            logger.info('Database connection closed')


if __name__ == '__main__':
    # Use container configuration when running in Docker environment
    section = 'postgresql_container' if os.getenv('DOCKER_ENV') else 'postgresql_test'
    connect(section)
