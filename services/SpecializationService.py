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

specialization_app = Blueprint('specialization_app', __name__)


# Specializations API
# university.specializations(@id, code, name, #department_id)
@specialization_app.route('/specializations/get', methods=['GET'])
def get_specializations():
    """ Get all specializations in JSON format """
    query = "SELECT * FROM university.specializations"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_specialization_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@specialization_app.route('/specializations/get/<int:id>', methods=['GET'])
def get_specialization_by_id(id):
    """ Get a specialization by ID in JSON format """
    query = "SELECT * FROM university.specializations WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_specialization_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@specialization_app.route('/specializations/identify', methods=['POST'])
def identify_specialization():
    """Identify a specialization by code in JSON format"""
    data = request.json
    code = data.get('code', '')

    query = "SELECT * FROM university.specializations WHERE code = '%(code)s' " % {'code': code}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_specialization_statement(row))

    return jsonify(returnStatement)

@specialization_app.route('/specializations/add', methods=['POST'])
def add_specialization():
    """ Add a specialization by data in JSON format """
    data = request.json

    code = data.get('code', '')
    name = data.get('name', '')
    department_id = data.get('department_id', '')

    query = "INSERT INTO university.specializations (code, name, department_id) VALUES ('%(code)s', '%(name)s', %(department_id)s) RETURNING id" % {'code': code, 'name': name, 'department_id': department_id}
    conn = connect_pg.connect()
    new_specialization_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_specialization_id:
        return jsonify({"message": "Specialization successfully added!"}), 200
    else:
        return jsonify({"message": "Specialization not found!"}), 404

@specialization_app.route('/specializations/delete/<int:id>', methods=['GET'])
def delete_specialization_by_id(id):
    """ Delete a specialization by ID in JSON format """
    query = "DELETE FROM university.specializations WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Specialization deleted successfully!"}), 200
    else:
        return jsonify({"message": "Specialization not found!"}), 404

def get_specialization_statement(row):
    """ Formats specialization data in JSON """
    return {
        'id': row[0],               # L'ID de la spécialisation
        'code': row[1],             # Le code de la spécialisation
        'name': row[2],             # Le nom de la spécialisation
        'department_id': row[3]     # L'ID du département associé à la spécialisation
    }
