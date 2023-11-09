#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# Departments API
# university.departments(@id, name, description, department_type)
@app.route('/departments/get', methods=['GET'])
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

@app.route('/departments/get/<int:id>', methods=['GET'])
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

@app.route('/departments/identify', methods=['POST'])
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

@app.route('/departments/add', methods=['POST'])
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

@app.route('/departments/delete/<int:id>', methods=['GET'])
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

# Groups API
# university.groups(@id, promotion, type, #department_id)
@app.route('/groups/get', methods=['GET'])
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

@app.route('/groups/get/<int:id>', methods=['GET'])
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

@app.route('/groups/identify', methods=['POST'])
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

@app.route('/groups/add', methods=['POST'])
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

@app.route('/groups/delete/<int:id>', methods=['GET'])
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

# Subgroups API
# university.subgroups(@id, name, #group_id)
@app.route('/subgroups/get', methods=['GET'])
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

@app.route('/subgroups/get/<int:id>', methods=['GET'])
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

@app.route('/subgroups/identify', methods=['POST'])
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

@app.route('/subgroups/add', methods=['POST'])
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

@app.route('/subgroups/delete/<int:id>', methods=['GET'])
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

# Personals API
# university.personals(@id, last_name, first_name, mail, phone_number)
@app.route('/personals/get', methods=['GET'])
def get_personals():
    """ Get all personals in JSON format """
    query = "SELECT * FROM university.personals"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_personal_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@app.route('/personals/get/<int:id>', methods=['GET'])
def get_personal_by_id(id):
    """ Get a personal by ID in JSON format """
    query = "SELECT * FROM university.personals WHERE id = %(id)s" % {'id': id}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_personal_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@app.route('/personals/identify', methods=['POST'])
def identify_personal():
    """Identify a personal by mail in JSON format"""
    data = request.json
    mail = data.get('mail', '')

    query = "SELECT * FROM university.personals WHERE mail = '%(mail)s'" % {'mail': mail}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn,query)
    connect_pg.disconnect(conn)

    returnStatement = []
    for row in rows:
        returnStatement.append(get_personal_statement(row))

    return jsonify(returnStatement)

@app.route('/personals/add', methods=['POST'])
def add_personal():
    """ Add a personal by data in JSON format """
    data = request.json

    last_name = data.get('last_name', '')
    first_name = data.get('first_name', '')
    mail = data.get('mail', '')
    phone_number = data.get('phone_number', '')

    query = "INSERT INTO university.personals (last_name, first_name, mail, phone_number) VALUES '(%(last_name)s', '%(first_name)s', '%(mail)s', '%(phone_number)s') RETURNING id" %  {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number}
    conn = connect_pg.connect()
    new_personal_id = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)

    if new_personal_id:
        return jsonify({"message": "Personal successfully added!"}), 200
    else:
        return jsonify({"message": "Personal not found!"}), 404

@app.route('/personals/delete/<int:id>', methods=['GET'])
def delete_personal_by_id(id):
    """ Delete a personal by ID in JSON format """
    query = "DELETE FROM university.personals WHERE id = %(id)s RETURNING id" %  {'id': id}
    conn = connect_pg.connect()
    row = connect_pg.execute_commands(conn, (query,))
    connect_pg.disconnect(conn)
    if row:
        return jsonify({"message": "Personal deleted successfully!"}), 200
    else:
        return jsonify({"message": "Personal not found!"}), 404

def get_personal_statement(row):
    """ Formats personal data in JSON """
    return {
        'id': row[0],              # L'ID du personnel
        'last_name': row[1],       # Le nom de famille du personnel
        'first_name': row[2],      # Le prénom du personnel
        'mail': row[3],            # L'adresse e-mail du personnel
        'phone_number': row[4]     # Le numéro de téléphone du personnel
    }

# Specializations API
# university.specializations(@id, code, name, #department_id)
@app.route('/specializations/get', methods=['GET'])
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

@app.route('/specializations/get/<int:id>', methods=['GET'])
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

@app.route('/specializations/identify', methods=['POST'])
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

@app.route('/specializations/add', methods=['POST'])
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

@app.route('/specializations/delete/<int:id>', methods=['GET'])
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

# Rooms API
# university.roles(@id, name, description, personal_id)
@app.route('/rooms/get', methods=['GET'])
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

@app.route('/rooms/get/<int:id>', methods=['GET'])
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

@app.route('/rooms/identify', methods=['POST'])
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

@app.route('/rooms/add', methods=['POST'])
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

@app.route('/rooms/delete/<int:id>', methods=['GET'])
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

# Teachings API
# university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
@app.route('/teachings/get', methods=['GET'])
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

@app.route('/teachings/get/<int:id>', methods=['GET'])
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

@app.route('/teachings/identify', methods=['POST'])
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

@app.route('/teachings/add', methods=['POST'])
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

@app.route('/teachings/delete/<int:id>', methods=['GET'])
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

# Roles API
# university.roles(@id, name, description, personal_id)
@app.route('/roles/get', methods=['GET'])
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

@app.route('/roles/get/<int:id>', methods=['GET'])
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

@app.route('/roles/identify', methods=['POST'])
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

@app.route('/roles/add', methods=['POST'])
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

@app.route('/roles/delete/<int:id>', methods=['GET'])
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

# Courses API
# university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
@app.route('/courses/get', methods=['GET'])
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

@app.route('/courses/get/<int:id>', methods=['GET'])
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

@app.route('/courses/identify', methods=['POST'])
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

@app.route('/courses/add', methods=['POST'])
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

@app.route('/courses/delete/<int:id>', methods=['GET'])
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

# Students API
# university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
@app.route('/students/get', methods=['GET'])
def get_students():
    query = "SELECT * FROM university.students"
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = []
    for row in rows:
        returnStatement.append(get_student_statement(row))
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@app.route('/students/get/<string:student_number>', methods=['GET'])
def get_student_by_id(student_number):
    query = "SELECT * FROM university.students WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
    conn = connect_pg.connect()
    rows = connect_pg.get_query(conn, query)
    returnStatement = {}
    if len(rows) > 0:
        returnStatement = get_student_statement(rows[0])
    connect_pg.disconnect(conn)
    return jsonify(returnStatement)

@app.route('/students/identify', methods=['POST'])
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

@app.route('/students/add', methods=['POST'])
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

@app.route('/students/delete/<string:student_number>', methods=['GET'])
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

if __name__ == "__main__":
    # read server parameters
    params = config('config.ini', 'server')
    # Launch Flask server
    app.run(debug=params['debug'], host=params['host'], port=params['port'])
    