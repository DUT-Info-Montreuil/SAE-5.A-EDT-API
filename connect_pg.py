#!/usr/bin/python
import psycopg2
from config import config
 
def connect(filename='config.ini', section='postgresql'):
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

if __name__ == '__main__':
    connect()