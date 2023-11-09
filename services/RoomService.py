from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

import connect_pg
import psycopg2
import requests
import hashlib
import json

room_app = Blueprint('room_app', __name__)

# Rooms API
# university.roles(@id, name, description, personal_id)
@room_app.route('/rooms/get', methods=['GET'])
def get_rooms():
    """ Get all rooms in JSON format """
    query = "SELECT * FROM university.rooms"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_room_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@room_app.route('/rooms/get/<int:id>', methods=['GET'])
def get_room_by_id(id):
    """ Get a room by ID in JSON format """
    query = "SELECT * FROM university.rooms WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_room_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@room_app.route('/rooms/identify', methods=['POST'])
def identify_room():
    """Identify a room by code in JSON format"""
    data = request.json
    code = data.get('code', '')

    query = "SELECT * FROM university.rooms WHERE code = '%(code)s'" % {'code': code}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn,query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_room_statement(row))

    return jsonify(returnStatement)

@room_app.route('/rooms/add', methods=['POST'])
def add_room():
    """ Add a room by data in JSON format """
    data = request.json

    code = data.get('code', '')
    capacity = data.get('capacity', '')
    has_computer = data.get('has_computer', '')
    has_projector = data.get('has_projector', '')

    query = "INSERT INTO university.rooms (code, capacity, has_computer, has_projector) VALUES ('%(code)s', %(capacity)s, '%(has_computer)s', '%(has_projector)s') RETURNING id" % {'code': code, 'capacity': capacity, 'has_computer': has_computer, 'has_projector': has_projector}
    conn = connect_pg.connect()
    new_room_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_room_id:
        return jsonify({"message": "Room successfully added!"}), 200
    else:
        return jsonify({"message": "Room not found!"}), 404

@room_app.route('/rooms/delete/<int:id>', methods=['GET'])
def delete_room_by_id(id):
    """ Delete a room by ID in JSON format """
    query = "DELETE FROM university.rooms WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Room deleted successfully!"}), 200
    else:
        return jsonify({"message": "Room not found!"}), 404

def get_room_statement(row):
    """ Formats room data in JSON """
    return {
        'id': row[0],              # L'ID de la salle
        'code': row[1],            # Le code de la salle
        'capacity': row[2],        # La capacité de la salle
        'has_computer': row[3],    # Indique si la salle a un ordinateur (true ou false)
        'has_projector': row[4]    # Indique si la salle a un projecteur (true ou false)
    }