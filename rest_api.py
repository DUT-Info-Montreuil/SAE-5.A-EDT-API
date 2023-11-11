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

from controllers.department_controller import department_app
from controllers.group_controller import group_app
from controllers.subgroup_controller import subgroup_app
from controllers.personal_controller import personal_app
from controllers.specialization_controller import specialization_app
from controllers.room_controller import room_app
from controllers.teaching_controller import teaching_app
from controllers.role_controller import role_app
from controllers.course_controller import course_app
from controllers.student_controller import student_app
from controllers.responsible_controller import responsible_app
from controllers.reminder_controller import reminder_app
from controllers.absent_controller import absent_app
from controllers.participate_controller import participate_app

# Register the main controller
app = Flask(__name__)

# Register the department controller
app.register_blueprint(department_app)

# Register the group controller
app.register_blueprint(group_app)

# Register the subgroup controller
app.register_blueprint(subgroup_app)

# Register the personal controller
app.register_blueprint(personal_app)

# Register the specialization controller
app.register_blueprint(specialization_app)

# Register the room controller
app.register_blueprint(room_app)

# Register the teaching controller
app.register_blueprint(teaching_app)

# Register the role controller
app.register_blueprint(role_app)

# Register the course controller
app.register_blueprint(course_app)

# Register the student controller
app.register_blueprint(student_app)

# Register the responsible controller
app.register_blueprint(responsible_app)

# Register the reminder controller
app.register_blueprint(reminder_app)

# Register the absent controller
app.register_blueprint(absent_app)

# Register the participate controller
app.register_blueprint(participate_app)


cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# CREATE ALL DB 
# !! Warning this methode drop all before !! 
# university()
@app.route('/create_university_db', methods=['GET'])
def create_university_db():
    """ CREATE ALL DB this methode will DROP all BEFORE create """
    # script_file_path = 'scripts/script_university.sql'
    # result = connect_pg.execute_sql_script(script_file_path)
    script_file_path = 'scripts/script_university_create.sql'
    result = connect_pg.execute_sql_script(script_file_path)
    
    script_file_path = 'scripts/script_university_school_insert.sql'
    result1 = connect_pg.execute_sql_script(script_file_path)
    
    script_file_path = 'scripts/script_university_student_insert.sql'
    result2 = connect_pg.execute_sql_script(script_file_path)
    return jsonify( {"univesity_create" : result, "school_insert" : result1, "student_insert" : result2})

@app.route('/create_table_university_db', methods=['GET'])
def create_table_university_db():
    """ DROP AND CREATE ALL TABLE IN DB """
    script_file_path = 'scripts/script_university_create.sql'
    result = connect_pg.execute_sql_script(script_file_path)
    return result

@app.route('/empty_table_university_db', methods=['GET'])
def empty_table_university_db():
    """ EMPTY ALL TABLE IN THE DB """
    script_file_path = 'scripts/script_university_delete.sql'
    result = connect_pg.execute_sql_script(script_file_path)
    return result

@app.route('/insert_table_university_db', methods=['GET'])
def insert_table_university_db():
    """ INSERT ALL TABLE IN THE DB """
    script_file_path = 'scripts/script_university_school_insert.sql'
    result1 = connect_pg.execute_sql_script(script_file_path)
    
    script_file_path = 'scripts/script_university_student_insert.sql'
    result2 = connect_pg.execute_sql_script(script_file_path)
    return jsonify( {"school_insert" : result1, "student_insert" : result2})

@app.route('/drop_table_university_db', methods=['GET'])
def drop_table_university_db():
    """ DROP ALL TABLE IN THE DB """
    script_file_path = 'scripts/script_university_drop.sql'
    result = connect_pg.execute_sql_script(script_file_path)
    return result

if __name__ == "__main__":
    # read server parameters
    params = config('config.ini', 'server')
    # Launch Flask server
    app.run(debug=params['debug'], host=params['host'], port=params['port'])
    