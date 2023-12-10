#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
from config import config
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlAlchemyController import initialize_app, get_table_objects, initialize_database,drop_database ,create_database ,insert_university_user ,insert_university_school ,insert_university_student ,insert_university_courses ,insert_university_participate

from controllers import *

# Register the main controller
app = Flask(__name__)

# === region : JWT ===
app.config["JWT_SECRET_KEY"] = "hcohen_aclaude_achetouani_bseydi_mtoure"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15) 
jwt = JWTManager(app)
# === endregion : JWT ===

# === region : SQLAlchemy ===
db = initialize_app(app)

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

# Register the autentification controller
app.register_blueprint(auth_app)

# Register the timetable controller
app.register_blueprint(timetable_app)

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/create_university_db', methods=['GET'])
def create_university_db():
    """!! Warning this methode drop all before !!  CREATE ALL DB this methode will DROP all BEFORE create """
    result_bool, resultString  = initialize_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@app.route('/create_table_university_db', methods=['GET'])
def create_table_university_db():
    """ DROP AND CREATE ALL TABLE IN DB """
    result_bool, resultString  = create_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@app.route('/insert_table_university_db', methods=['GET'])
def insert_table_university_db():
    """ INSERT IN ALL TABLE IN THE DB """
    
    university_user_result_bool, university_user_result_string  = insert_university_user()
    university_school_result_bool, university_school_result_string  = insert_university_school()
    university_student_result_bool, university_student_result_string  = insert_university_student()
    university_courses_result_bool, university_courses_result_string  = insert_university_courses()
    university_participate_result_bool, university_participate_result_string  = insert_university_participate()
    result_bool = university_user_result_bool and university_school_result_bool and university_student_result_bool and university_courses_result_bool and university_participate_result_bool
    result = {"university_user" : university_user_result_string ,
        "university_school" : university_school_result_string ,
        "university_student" : university_student_result_string ,
        "university_courses" : university_courses_result_string ,
        "university_participate" : university_participate_result_string }

    print(f"Execute : {result_bool}")
    return jsonify(result)

@app.route('/drop_table_university_db', methods=['GET'])
def drop_table_university_db():
    """ DROP ALL TABLE IN THE DB """
    result_bool, resultString  = drop_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)


table_users, table_students, table_departments, table_groups, table_subgroups, table_personals, table_roles, table_courses, table_rooms, table_reminders, table_specializations, table_teachings, table_absents, table_participates, table_responsibles = get_table_objects(app)

class User(db.Model):
    __table__ = table_users

class Student(db.Model):
    __table__ = table_students

class Department(db.Model):
    __table__ = table_departments

class Group(db.Model):
    __table__ = table_groups

class Subgroup(db.Model):
    __table__ = table_subgroups

class Personal(db.Model):
    __table__ = table_personals

class Role(db.Model):
    __table__ = table_roles

class Course(db.Model):
    __table__ = table_courses

class Room(db.Model):
    __table__ = table_rooms

class Reminder(db.Model):
    __table__ = table_reminders

class Specialization(db.Model):
    __table__ = table_specializations

class Teaching(db.Model):
    __table__ = table_teachings

class Absent(db.Model):
    __table__ = table_absents

class Participate(db.Model):
    __table__ = table_participates

class Responsible(db.Model):
    __table__ = table_responsibles

# Route to get all users
@app.route('/test', methods=['GET'])
def get_all_users():
    users = Student.query.all()
    users_list = [{'last_name': user.last_name, 'first_name': user.first_name} for user in users]

    return jsonify({'users': users_list})

if __name__ == "__main__":
    # read server parameters
    params = config('config.ini', 'server')
    # Launch Flask server
    app.run(debug=params['debug'], host=params['host'], port=params['port'])
    create_university_db()