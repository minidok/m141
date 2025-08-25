#!/usr/bin/python
from configparser import ConfigParser
import os


def config(filename='dbconnection.ini', section='postgresql_test'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    # Override with environment variables if available (more secure)
    env_mappings = {
        'host': 'POSTGRES_HOST',
        'dbname': 'POSTGRES_DB', 
        'user': 'POSTGRES_USER',
        'password': 'POSTGRES_PASSWORD',
        'port': 'POSTGRES_PORT'
    }
    
    for db_key, env_key in env_mappings.items():
        if env_key in os.environ:
            db[db_key] = os.environ[env_key]
    
    # Set secure defaults
    if 'sslmode' not in db:
        db['sslmode'] = 'prefer'
    
    # Remove password from logs for security
    safe_db = db.copy()
    if 'password' in safe_db:
        safe_db['password'] = '***'
    print(f"Database config loaded: {safe_db}")
    
    return db