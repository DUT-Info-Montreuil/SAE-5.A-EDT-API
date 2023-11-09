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

department_app = Blueprint('department_app', __name__)

# Departments API
# university.departments(@id, name, description, department_type)
@department_app.route('/departments/get', methods=['GET'])
def get_departments():
    """ Get all department in JSON format """
    query = "SELECT * FROM university.departments"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_department_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@department_app.route('/departments/get/<int:id>', methods=['GET'])
def get_department_by_id(id):
    """ Get a department by ID in JSON format """
    query = "SELECT * FROM university.departments WHERE id = %(id)s" %  {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_department_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@department_app.route('/departments/identify', methods=['POST'])
def identify_department():
    """Identify a department by name and degree_type in JSON format"""
    data = request.json
    name = data.get('name', '')
    degree_type = data.get('degree_type', '')

    query = "SELECT * FROM university.departments WHERE name = '%(name)s' AND degree_type = '%(degree_type)s'" % {'name': name, 'degree_type': degree_type}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_department_statement(row))

    return jsonify(returnStatement)

@department_app.route('/departments/add', methods=['POST'])
def add_department():
    """ Add a department by data in JSON format """
    data = request.json

    name = data.get('name', '')
    description = data.get('description', '')
    degree_type = data.get('degree_type', '')
    personal_id = data.get('personal_id', '')

    query = "INSERT INTO university.departments (name, description, degree_type, personal_id) VALUES ('%(name)s', '%(description)s', '%(degree_type)s', %(personal_id)s) RETURNING id" %  {'name': name, 'description': description, 'degree_type': degree_type, 'personal_id': personal_id}
    conn = connect_pg.connect()
    new_department_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if new_department_id:
        return jsonify({"message": "Department successfully added!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404

@department_app.route('/departments/delete/<int:id>', methods=['GET'])
def delete_department_by_id(id):
    """ Delete a department by ID in JSON format """
    query = "DELETE FROM university.departments WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    print(row)
    if row:
        return jsonify({"message": "Department deleted successfully!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404

def get_department_statement(row):
    """ Formats department data in JSON"""
    return {
        'id': row[0],              # L'ID du département
        'name': row[1],            # Le nom du département
        'description': row[2],     # La description du département
        'degree_type': row[3],     # Le type de diplôme du département
        'personal_id': row[4]      # L'ID du personnel associé au département
    }