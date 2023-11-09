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

teaching_app = Blueprint('teaching_app', __name__)

# Teachings API
# university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
@teaching_app.route('/teachings/get', methods=['GET'])
def get_teachings():
    """ Get all teachings in JSON format """
    query = "SELECT * FROM university.teachings"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_teaching_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@teaching_app.route('/teachings/get/<int:id>', methods=['GET'])
def get_teaching_by_id(id):
    """ Get a teaching by ID in JSON format """
    query = "SELECT * FROM university.teachings WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_teaching_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@teaching_app.route('/teachings/identify', methods=['POST'])
def identify_teaching():
    """Identify a teaching by title, hour_number, semestre, sequence, and specialization_id in JSON format"""
    data = request.json
    title = data.get('title', '')
    hour_number = data.get('hour_number', '')
    semestre = data.get('semestre', '')
    sequence = data.get('sequence', '')
    specialization_id = data.get('specialization_id', '')

    query = "SELECT * FROM university.teachings WHERE title = '%(title)s' AND hour_number = %(hour_number)s AND semestre = %(semestre)s AND sequence = '%(sequence)s' AND specialization_id = %(specialization_id)s" % {'title': title, 'hour_number': hour_number, 'semestre': semestre, 'sequence': sequence, 'specialization_id': specialization_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_teaching_statement(row))

    return jsonify(returnStatement)

@teaching_app.route('/teachings/add', methods=['POST'])
def add_teaching():
    """ Add a teaching by data in JSON format """
    data = request.json

    title = data.get('title', '')
    hour_number = data.get('hour_number', '')
    semestre = data.get('semestre', '')
    sequence = data.get('sequence', '')
    description = data.get('description', '')
    teaching_type = data.get('teaching_type', '')
    specialization_id = data.get('specialization_id', '')

    query = "INSERT INTO university.teachings (title, hour_number, semestre, sequence, description, teaching_type, specialization_id) VALUES ('%(title)s', %(hour_number)s, %(semestre)s, '%(sequence)s', '%(description)s', '%(teaching_type)s,' %(specialization_id)s) RETURNING id" % {'title': title, 'hour_number': hour_number, 'semestre': semestre, 'sequence': sequence, 'description': description, 'teaching_type': teaching_type, 'specialization_id': specialization_id}
    conn = connect_pg.connect()
    new_teaching_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_teaching_id:
        return jsonify({"message": "Teaching successfully added!"}), 200
    else:
        return jsonify({"message": "Teaching not found!"}), 404

@teaching_app.route('/teachings/delete/<int:id>', methods=['GET'])
def delete_teaching_by_id(id):
    """ Delete a teaching by ID in JSON format """
    query = "DELETE FROM university.teachings WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Teaching deleted successfully!"}), 200
    else:
        return jsonify({"message": "Teaching not found!"}), 404

def get_teaching_statement(row):
    """ Formats teaching data in JSON """
    return {
        'id': row[0],                   # L'ID de l'enseignement
        'title': row[1],                # Le titre de l'enseignement
        'hour_number': row[2],          # Le nombre d'heures
        'semestre': row[3],             # Le semestre
        'sequence': row[4],             # La séquence
        'description': row[5],          # La description
        'teaching_type': row[6],        # Le type d'enseignement
        'specialization_id': row[7]     # L'ID de la spécialisation associée à l'enseignement
    }