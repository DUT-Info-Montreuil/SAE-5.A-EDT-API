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

personal_app = Blueprint('personal_app', __name__)

# Personals API
# university.personals(@id, last_name, first_name, mail, phone_number)
@personal_app.route('/personals/get', methods=['GET'])
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

@personal_app.route('/personals/get/<int:id>', methods=['GET'])
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

@personal_app.route('/personals/identify', methods=['POST'])
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

@personal_app.route('/personals/add', methods=['POST'])
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

@personal_app.route('/personals/delete/<int:id>', methods=['GET'])
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