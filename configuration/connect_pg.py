#!/usr/bin/python
import psycopg2
from configuration.config import config
 
def connect(filename='configuration/config.ini', section='postgresql'):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config(filename, section)
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return conn

def disconnect(conn):
    conn.close()
    print('Database connection closed.')

def execute_commands(conn, commands):
    """ Execute a SQL command """
    cur = conn.cursor()

    returningValue = False 

    # create table one by one
    for command in commands:
        if command :
            print(command)
            cur.execute(command)
            if " returning " in command.lower(): 
                returningValue = cur.fetchone()[0]
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit() 
    if returningValue:
        return returningValue

def get_query(conn, query):
    """ query data from db """
    try:
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall() 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            return rows

def execute_sql_script(script_file,filename='config.ini', section='postgresql'):
    """Execute an SQL script to the database."""
    
    result = True ,"SQL script executed successfully."
    try:
        params = config(filename, section)
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor()
        
        with open(script_file, 'r') as sql_file:
            sql_script = sql_file.read()
            cur.execute(sql_script)

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error executing SQL script:", error)
        result = False ,"Error executing SQL script:"

    finally:
        cur.close()
        conn.close()
        
    return result
        
        
if __name__ == '__main__':
    connect()