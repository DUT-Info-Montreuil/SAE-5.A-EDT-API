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

course_app = Blueprint('course_app', __name__)

# Courses API
# university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
@course_app.route('/courses/get', methods=['GET'])
def get_courses():
    """ Get all courses in JSON format """
    query = "SELECT * FROM university.courses"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_course_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@course_app.route('/courses/get/<int:id>', methods=['GET'])
def get_course_by_id(id):
    """ Get a course by ID in JSON format """
    query = "SELECT * FROM university.courses WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_course_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@course_app.route('/courses/identify', methods=['POST'])
def identify_course():
    """Identify a course by description, starttime, duree, course_type, personal_id, and rooms_id in JSON format"""
    data = request.json
    starttime = data.get('starttime', '')
    teaching_id = data.get('teaching_id', '')
    personal_id = data.get('personal_id', '')
    rooms_id = data.get('rooms_id', '')

    query = "SELECT * FROM university.courses WHERE starttime = '%(starttime)s' AND teaching_id = %(teaching_id)s AND personal_id = %(personal_id)s AND rooms_id = %(rooms_id)s" %  {'starttime': starttime, 'personal_id': personal_id,'teaching_id': teaching_id, 'rooms_id': rooms_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_course_statement(row))

    return jsonify(returnStatement)

@course_app.route('/courses/add', methods=['POST'])
def add_course():
    """ Add a course by data in JSON format """
    data = request.json

    description = data.get('description', '')
    starttime = data.get('starttime', '')
    duree = data.get('duree', '')
    course_type = data.get('course_type', '')
    personal_id = data.get('personal_id', '')
    rooms_id = data.get('rooms_id', '')
    teaching_id = data.get('teaching_id', '')

    query = "INSERT INTO university.courses (description, starttime, duree, course_type, personal_id, rooms_id, teaching_id) VALUES ('%(description)s', '%(starttime)s', '%(duree)s', '%(course_type)s', %(personal_id)s, %(rooms_id)s, %(teaching_id)s) RETURNING id" % {'description': description, 'starttime': starttime, 'duree': duree, 'course_type': course_type, 'personal_id': personal_id, 'rooms_id': rooms_id, 'teaching_id': teaching_id}
    conn = connect_pg.connect()
    new_course_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_course_id:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@course_app.route('/courses/delete/<int:id>', methods=['GET'])
def delete_course_by_id(id):
    """ Delete a course by ID in JSON format """
    query = "DELETE FROM university.courses WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

def get_course_statement(row):
    """ Formats course data in JSON """
    return {
        'id': row[0],              # L'ID du cours
        'description': row[1],     # La description du cours
        'starttime': row[2],       # L'heure de début du cours
        'duree': row[3],           # La durée du cours
        'course_type': row[4],     # Le type de cours
        'personal_id': row[5],     # L'ID du personnel associé au cours
        'rooms_id': row[6],        # L'ID de la salle associée au cours
        'teaching_id': row[7]      # L'ID de l'enseignement associé au cours
    }