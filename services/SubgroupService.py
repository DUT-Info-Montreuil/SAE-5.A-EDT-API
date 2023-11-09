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

subgroup_app = Blueprint('subgroup_app', __name__)

# Subgroups API
# university.subgroups(@id, name, #group_id)
@subgroup_app.route('/subgroups/get', methods=['GET'])
def get_subgroups():
    """ Get all subgroups in JSON format """
    query = "SELECT * FROM university.subgroups"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_subgroup_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/get/<int:id>', methods=['GET'])
def get_subgroup_by_id(id):
    """ Get a subgroup by ID in JSON format """
    query = "SELECT * FROM university.subgroups WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_subgroup_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/identify', methods=['POST'])
def identify_subgroup():
    """Identify a subgroup by name and group_id in JSON format"""
    data = request.json
    name = data.get('name', '')
    group_id = data.get('group_id', '')

    query = "SELECT * FROM university.subgroups WHERE name = '%(name)s' AND group_id = %(group_id)s" % {'name': name, 'group_id': group_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_subgroup_statement(row))

    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/add', methods=['POST'])
def add_subgroup():
    """ Add a subgroup by data in JSON format """
    data = request.json

    name = data.get('name', '')
    group_id = data.get('group_id', '')

    query = "INSERT INTO university.subgroups (name, group_id) VALUES ('%(name)s', %(group_id)s) RETURNING id" % {'name': name, 'group_id': group_id}
    conn = connect_pg.connect()
    new_subgroup_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_subgroup_id:
        return jsonify({"message": "Subgroup successfully added!"}), 200
    else:
        return jsonify({"message": "Subgroup not found!"}), 404

@subgroup_app.route('/subgroups/delete/<int:id>', methods=['GET'])
def delete_subgroup_by_id(id):
    """ Delete a subgroup by ID in JSON format """
    query = "DELETE FROM university.subgroups WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Subgroup deleted successfully!"}), 200
    else:
        return jsonify({"message": "Subgroup not found!"}), 404

def get_subgroup_statement(row):
    """ Formats subgroup data in JSON"""
    return {
        'id': row[0],              # L'ID du sous-groupe
        'name': row[1],            # Le nom du sous-groupe
        'group_id': row[2]         # L'ID du groupe associé au sous-groupe
    }
