#!/usr/bin/python
# Datenbank Verbindung mit postgres DB aufbauen
## Beschreibung Modul https://www.psycopg.org/psycopg3/docs/basic/usage.html
## Psycopg 3 – PostgreSQL database adapter for Python
import psycopg
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # Eigenes modul config.py einlesen
        params = config()

        # Verbdinung zum PostgreSQL server herstellen
        print('Connecting to the PostgreSQL database...')
        conn = psycopg.connect(**params)
		
        # Cursor auf die Datenbank erhalten
        cur = conn.cursor()
        
	    # Mit dem Cursor ein Query ausführen
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Antwort zum Query vom Server holen, als einen Datensatz
        db_version = cur.fetchone()
        print(db_version)
       
	    # Verbindung zum Server PostgreSQL schliessen
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
