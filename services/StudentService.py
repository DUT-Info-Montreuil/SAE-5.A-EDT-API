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

student_app = Blueprint('student_app', __name__)

# Students API
# university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
@student_app.route('/students/get', methods=['GET'])
def get_students():
    query = "SELECT * FROM university.students"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_student_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@student_app.route('/students/get/<string:student_number>', methods=['GET'])
def get_student_by_id(student_number):
    query = "SELECT * FROM university.students WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_student_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@student_app.route('/students/identify', methods=['POST'])
def identify_student():
    data = request.json
    last_name = data.get('last_name', '')
    first_name = data.get('first_name', '')
    mail = data.get('mail', '')
    phone_number = data.get('phone_number', '')
    department_id = data.get('department_id', '')
    group_id = data.get('group_id', '')
    subgroup_id = data.get('subgroup_id', '')

    query = "SELECT * FROM university.students WHERE last_name = '%(last_name)s' AND first_name = '%(first_name)s' AND mail = '%(mail)s' AND phone_number = '%(phone_number)s' AND department_id = %(department_id)s AND group_id = %(group_id)s AND subgroup_id = %(subgroup_id)s" % {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number, 'department_id': department_id, 'group_id': group_id, 'subgroup_id': subgroup_id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_student_statement(row))

    return jsonify(returnStatement)

@student_app.route('/students/add', methods=['POST'])
def add_student():
    data = request.json

    student_number = data.get('student_number', '')
    last_name = data.get('last_name', '')
    first_name = data.get('first_name', '')
    mail = data.get('mail', '')
    phone_number = data.get('phone_number', '')
    department_id = data.get('department_id', '')
    group_id = data.get('group_id', '')
    subgroup_id = data.get('subgroup_id', '')

    query = "INSERT INTO university.students (student_number, last_name, first_name, mail, phone_number, department_id, group_id, subgroup_id) VALUES ('%(student_number)s', '%(last_name)s', '%(first_name)s', '%(mail)s', '%(phone_number)s', %(department_id)s, %(group_id)s, %(subgroup_id)s) RETURNING id" % {'student_number': student_number, 'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number, 'department_id': department_id, 'group_id': group_id, 'subgroup_id': subgroup_id}
    conn = connect_pg.connect()
    new_student_number = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_student_number:
        return jsonify({"message": "Student successfully added!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

@student_app.route('/students/delete/<string:student_number>', methods=['GET'])
def delete_student_by_id(student_number):
    query = "DELETE FROM university.students WHERE student_number = '%(student_number)s' RETURNING student_number" %  {'student_number': student_number}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Student deleted successfully!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

def get_student_statement(row):
    return {
        'student_number': row[0],    # Numero étudiant
        'last_name': row[1],         # Le nom de famille de l'étudiant
        'first_name': row[2],        # Le prénom de l'étudiant
        'mail': row[3],              # L'adresse e-mail de l'étudiant
        'phone_number': row[4],      # Le numéro de téléphone de l'étudiant
        'department_id': row[5],     # L'ID du département auquel l'étudiant est affilié
        'group_id': row[6],          # L'ID du groupe auquel l'étudiant appartient
        'subgroup_id': row[7]        # L'ID du sous-groupe auquel l'étudiant est associé
    }