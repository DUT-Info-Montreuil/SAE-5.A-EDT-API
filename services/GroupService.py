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

group_app = Blueprint('group_app', __name__)

# Groups API
# university.groups(@id, promotion, type, #department_id)
@group_app.route('/groups/get', methods=['GET'])
def get_groups():
    """ Get all groups in JSON format """
    query = "SELECT * FROM university.groups"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_group_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@group_app.route('/groups/get/<int:id>', methods=['GET'])
def get_group_by_id(id):
    """ Get a group by ID in JSON format """
    query = "SELECT * FROM university.groups WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_group_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@group_app.route('/groups/identify', methods=['POST'])
def identify_group():
    """Identify a group by promotion and type in JSON format"""
    data = request.json
    
    promotion = data.get('promotion', '')
    group_type = data.get('type', '')
    department_id = data.get('department_id', '')

    query = "SELECT * FROM university.groups WHERE promotion = %(promotion)s AND type = '%(type)s' AND department_id = %(department_id)s" %  {'promotion': promotion, 'type': group_type, 'department_id': department_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_group_statement(row))

    return jsonify(returnStatement)

@group_app.route('/groups/add', methods=['POST'])
def add_group():
    """ Add a group by data in JSON format """
    data = request.json

    promotion = data.get('promotion', '')
    group_type = data.get('type', '')
    department_id = data.get('department_id', '')

    query = "INSERT INTO university.groups (promotion, type, department_id) VALUES (%(promotion)s, '%(type)s', %(department_id)s) RETURNING id" % {'promotion': promotion, 'type': group_type, 'department_id': department_id}
    conn = connect_pg.connect()
    new_group_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_group_id:
        return jsonify({"message": "Group successfully added!"}), 200
    else:
        return jsonify({"message": "Group not found!"}), 404

@group_app.route('/groups/delete/<int:id>', methods=['GET'])
def delete_group_by_id(id):
    """ Delete a group by ID in JSON format """
    query = "DELETE FROM university.groups WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Department deleted successfully!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404

def get_group_statement(row):
    """ Formats group data in JSON"""
    return {
        'id': row[0],              # L'ID du groupe
        'promotion': row[1],       # La promotion du groupe
        'type': row[2],            # Le type du groupe
        'department_id': row[3]    # L'ID du département associé au groupe
    }