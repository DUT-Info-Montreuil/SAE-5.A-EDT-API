from services.main_service import Service

import connect_pg
import psycopg2
import requests
import hashlib
import json

class personal_service(Service):
    
    # Personals API
    # university.personals(@id, last_name, first_name, mail, phone_number)
    def get_personals(self):
        """ Get all personals in JSON format """
        query = "SELECT * FROM university.personals"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_personal_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_personal_by_id(self, id):
        """ Get a personal by ID in JSON format """
        query = "SELECT * FROM university.personals WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_personal_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_personal(self, data):
        """Identify a personal by mail in JSON format"""
        # data = request.json
        mail = data.get('mail', '')
    
        query = "SELECT * FROM university.personals WHERE mail = '%(mail)s'" % {'mail': mail}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn,query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_personal_statement(row))
    
        return returnStatement
    
    def add_personal(self, data):
        """ Add a personal by data in JSON format """
        # data = request.json
    
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
    
        query = "INSERT INTO university.personals (last_name, first_name, mail, phone_number) VALUES '(%(last_name)s', '%(first_name)s', '%(mail)s', '%(phone_number)s') RETURNING id" %  {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number}
        conn = self.get_connection()
        new_personal_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_personal_id
    
    def delete_personal_by_id(self, id):
        """ Delete a personal by ID in JSON format """
        query = "DELETE FROM university.personals WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def get_personal_statement(self, row):
        """ Formats personal data in JSON """
        return {
            'id': row[0],              # L'ID du personnel
            'last_name': row[1],       # Le nom de famille du personnel
            'first_name': row[2],      # Le prénom du personnel
            'mail': row[3],            # L'adresse e-mail du personnel
            'phone_number': row[4]     # Le numéro de téléphone du personnel
        }