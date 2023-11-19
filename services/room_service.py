from entities.dto.Room import Room
from services.main_service import Service

import connect_pg
import psycopg2
import requests
import hashlib
import json

class room_service(Service):
    
    # Rooms API
    # university.roles(@id, name, description, personal_id)
    def get_rooms(self):
        """ Get all rooms in JSON format """
        query = "SELECT * FROM university.rooms"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(Room.objectify(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_room_by_id(self, id):
        """ Get a room by ID in JSON format """
        query = "SELECT * FROM university.rooms WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = Room.objectify(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_room(self, data):
        """Identify a room by code in JSON format"""
        # data = request.json
        code = data.get('code', '')
    
        query = "SELECT * FROM university.rooms WHERE code = '%(code)s'" % {'code': code}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn,query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(Room.objectify(row))
    
        return returnStatement
    
    def add_room(self, data):
        """ Add a room by data in JSON format """
        # data = request.json
    
        code = data.get('code', '')
        capacity = data.get('capacity', '')
        has_computer = data.get('has_computer', '')
        has_projector = data.get('has_projector', '')
    
        query = "INSERT INTO university.rooms (code, capacity, has_computer, has_projector) VALUES ('%(code)s', %(capacity)s, '%(has_computer)s', '%(has_projector)s') RETURNING id" % {'code': code, 'capacity': capacity, 'has_computer': has_computer, 'has_projector': has_projector}
        conn = self.get_connection()
        new_room_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_room_id
    
    def delete_room_by_id(self, id):
        """ Delete a room by ID in JSON format """
        query = "DELETE FROM university.rooms WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_room(self, id, data):
        """ Update a room record by ID using data in JSON format """
        # data = request.json

        # Check if the room record with the given ID exists
        existing_room = self.get_room_by_id(id)
        if not existing_room:
            return existing_room

        code = data.get('code', existing_room['code'])
        capacity = data.get('capacity', existing_room['capacity'])
        has_computer = data.get('has_computer', existing_room['has_computer'])
        has_projector = data.get('has_projector', existing_room['has_projector'])

        query = """UPDATE university.rooms
                SET code = '%(code)s',
                    capacity = %(capacity)s,
                    has_computer = '%(has_computer)s',
                    has_projector = '%(has_projector)s'
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'code': code,
                    'capacity': capacity,
                    'has_computer': has_computer,
                    'has_projector': has_projector
                }

        conn = self.get_connection()
        updated_room_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_room_id