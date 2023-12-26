#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from datetime import timedelta
from config import config

import connect_pg
from controllers import *

from flask_swagger_ui import get_swaggerui_blueprint

# Register the main controller
app = Flask(__name__)

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

# Config JWT
app.config["JWT_SECRET_KEY"] = "hcohen_aclaude_achetouani_bseydi_mtoure"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15) 
jwt = JWTManager(app)

app.register_blueprint(department_app)
app.register_blueprint(group_app)
app.register_blueprint(subgroup_app)
app.register_blueprint(personal_app)
app.register_blueprint(specialization_app)
app.register_blueprint(room_app)
app.register_blueprint(teaching_app)
app.register_blueprint(role_app)
app.register_blueprint(course_app)
app.register_blueprint(student_app)
app.register_blueprint(responsible_app)
app.register_blueprint(reminder_app)
app.register_blueprint(absent_app)
app.register_blueprint(participate_app)
app.register_blueprint(auth_app)
app.register_blueprint(user_app)

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
    
    script_file_path = 'scripts/script_university_user_insert.sql'
    result1 = connect_pg.execute_sql_script(script_file_path)
    
    
    script_file_path = 'scripts/script_university_school_insert.sql'
    result2 = connect_pg.execute_sql_script(script_file_path)
    
    script_file_path = 'scripts/script_university_student_insert.sql'
    result3 = connect_pg.execute_sql_script(script_file_path)
    
    script_file_path = 'scripts/script_university_courses_insert.sql'
    result4 = connect_pg.execute_sql_script(script_file_path)

    script_file_path = 'scripts/script_university_participate_insert.sql'
    result5 = connect_pg.execute_sql_script(script_file_path)
    
    return jsonify( {"univesity_create" : result, "user_insert" : result1, "school_insert" : result2, "student_insert" : result3, "courses_insert" : result4, "participate_insert" : result5})

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
    create_university_db()
    