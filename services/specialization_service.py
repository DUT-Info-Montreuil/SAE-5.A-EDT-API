from services.main_service import Service

import connect_pg
import psycopg2
import requests
import hashlib
import json

class specialization_service(Service):
    
    
    # Specializations API
    # university.specializations(@id, code, name, #department_id)
    def get_specializations(self):
        """ Get all specializations in JSON format """
        query = "SELECT * FROM university.specializations"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_specialization_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_specialization_by_id(self, id):
        """ Get a specialization by ID in JSON format """
        query = "SELECT * FROM university.specializations WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_specialization_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_specialization(self, data):
        """Identify a specialization by code in JSON format"""
        # data = request.json
        code = data.get('code', '')
    
        query = "SELECT * FROM university.specializations WHERE code = '%(code)s' " % {'code': code}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_specialization_statement(row))
    
        return returnStatement
    
    def add_specialization(self, data):
        """ Add a specialization by data in JSON format """
        # data = request.json
    
        code = data.get('code', '')
        name = data.get('name', '')
        department_id = data.get('department_id', '')
    
        query = "INSERT INTO university.specializations (code, name, department_id) VALUES ('%(code)s', '%(name)s', %(department_id)s) RETURNING id" % {'code': code, 'name': name, 'department_id': department_id}
        conn = self.get_connection()
        new_specialization_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_specialization_id
    
    def delete_specialization_by_id(self, id):
        """ Delete a specialization by ID in JSON format """
        query = "DELETE FROM university.specializations WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def get_specialization_statement(self, row):
        """ Formats specialization data in JSON """
        return {
            'id': row[0],               # L'ID de la spécialisation
            'code': row[1],             # Le code de la spécialisation
            'name': row[2],             # Le nom de la spécialisation
            'department_id': row[3]     # L'ID du département associé à la spécialisation
        }
    