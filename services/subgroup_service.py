
from services.main_service import Service

import connect_pg
import psycopg2
import requests
import hashlib
import json

class subgroup_service(Service):
    
    # Subgroups API
    # university.subgroups(@id, name, #group_id)
    def get_subgroups(self):
        """ Get all subgroups in JSON format """
        query = "SELECT * FROM university.subgroups"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_subgroup_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_subgroup_by_id(self, id):
        """ Get a subgroup by ID in JSON format """
        query = "SELECT * FROM university.subgroups WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_subgroup_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_subgroup(self, data):
        """Identify a subgroup by name and group_id in JSON format"""
        # data = request.json
        name = data.get('name', '')
        group_id = data.get('group_id', '')
    
        query = "SELECT * FROM university.subgroups WHERE name = '%(name)s' AND group_id = %(group_id)s" % {'name': name, 'group_id': group_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_subgroup_statement(row))
    
        return returnStatement
    
    def add_subgroup(self, data):
        """ Add a subgroup by data in JSON format """
        # data = request.json
    
        name = data.get('name', '')
        group_id = data.get('group_id', '')
    
        query = "INSERT INTO university.subgroups (name, group_id) VALUES ('%(name)s', %(group_id)s) RETURNING id" % {'name': name, 'group_id': group_id}
        conn = self.get_connection()
        new_subgroup_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_subgroup_id
    
    def delete_subgroup_by_id(self, id):
        """ Delete a subgroup by ID in JSON format """
        query = "DELETE FROM university.subgroups WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def get_subgroup_statement(self, row):
        """ Formats subgroup data in JSON"""
        return {
            'id': row[0],              # L'ID du sous-groupe
            'name': row[1],            # Le nom du sous-groupe
            'group_id': row[2]         # L'ID du groupe associé au sous-groupe
        }
    