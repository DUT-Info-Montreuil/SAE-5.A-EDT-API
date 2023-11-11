import connect_pg
import psycopg2
import requests
import hashlib
import json


class Service:
    
    connection = None

    def get_connection(self):
        if(self.connection == None):
            self.connection = connect_pg.connect()
        return self.connection

    def connect(self):
        self.connection = connect_pg.connect()
        
    def disconnect(self):
        connect_pg.disconnect(self.connection)
        self.connection = None

