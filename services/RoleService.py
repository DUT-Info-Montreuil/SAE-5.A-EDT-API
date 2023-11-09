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

role_app = Blueprint('role_app', __name__)

# Roles API
# university.roles(@id, name, description, personal_id)
@role_app.route('/roles/get', methods=['GET'])
def get_roles():
    """ Get all roles in JSON format """
    query = "SELECT * FROM university.roles"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_role_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@role_app.route('/roles/get/<int:id>', methods=['GET'])
def get_role_by_id(id):
    """ Get a role by ID in JSON format """
    query = "SELECT * FROM university.roles WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_role_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@role_app.route('/roles/identify', methods=['POST'])
def identify_role():
    """Identify a role by name, and personal_id in JSON format"""
    data = request.json
    name = data.get('name', '')
    personal_id = data.get('personal_id', '')

    query = "SELECT * FROM university.roles WHERE name = '%(name)s' AND personal_id = %(personal_id)s" %  {'name': name, 'personal_id': personal_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn,query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_role_statement(row))

    return jsonify(returnStatement)

@role_app.route('/roles/add', methods=['POST'])
def add_role():
    """ Add a role by data in JSON format """
    data = request.json

    name = data.get('name', '')
    description = data.get('description', '')
    personal_id = data.get('personal_id', '')

    query = "INSERT INTO university.roles (name, description, personal_id) VALUES ('%(name)s', '%(description)s', %(personal_id)s) RETURNING id" %  {'name': name, 'description': description, 'personal_id': personal_id}
    conn = connect_pg.connect()
    new_role_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_role_id:
        return jsonify({"message": "Role successfully added!"}), 200
    else:
        return jsonify({"message": "Role not found!"}), 404

@role_app.route('/roles/delete/<int:id>', methods=['GET'])
def delete_role_by_id(id):
    """ Delete a role by ID in JSON format """
    query = "DELETE FROM university.roles WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Role deleted successfully!"}), 200
    else:
        return jsonify({"message": "Role not found!"}), 404

def get_role_statement(row):
    """ Formats role data in JSON """
    return {
        'id': row[0],              # L'ID du rôle
        'name': row[1],            # Le nom du rôle
        'description': row[2],     # La description du rôle
        'personal_id': row[3]      # L'ID du personnel associé au rôle
    }