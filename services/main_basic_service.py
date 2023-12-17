from services.sql_alchemy_service import db
from configuration import connect_pg
from entities.models.models import *

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