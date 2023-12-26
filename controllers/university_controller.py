#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify ,Blueprint
from services.university_service import university_service
from entities.models.models import *

university_app = Blueprint('university_app', __name__)
universityService = university_service()

@university_app.route('/create_university_db', methods=['GET'])
def create_university_db():
    """!! Warning this methode drop all before !!  CREATE ALL DB this methode will DROP all BEFORE create """
    result_bool, resultString  = universityService.initialize_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@university_app.route('/create_sample_university', methods=['GET'])
def create_sample_university():
    """!! Warning this methode drop all before !!  CREATE ALL DB this methode will DROP all BEFORE create """
    result_bool, resultString  = universityService.sample_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@university_app.route('/create_table_university_db', methods=['GET'])
def create_table_university_db():
    """ DROP AND CREATE ALL TABLE IN DB """
    result_bool, resultString  = universityService.create_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString) 

@university_app.route('/insert_table_university_db', methods=['GET'])
def insert_table_university_db():
    """ INSERT IN ALL TABLE IN THE DB """
    university_user_result_bool, university_user_result_string  = universityService.insert_university_user()
    university_school_result_bool, university_school_result_string  = universityService.insert_university_school()
    university_student_result_bool, university_student_result_string  = universityService.insert_university_student()
    university_courses_result_bool, university_courses_result_string  = universityService.insert_university_courses()
    university_participate_result_bool, university_participate_result_string  = universityService.insert_university_participate()
    result_bool = university_user_result_bool and university_school_result_bool and university_student_result_bool and university_courses_result_bool and university_participate_result_bool
    result = {"university_user" : university_user_result_string ,
        "university_school" : university_school_result_string ,
        "university_student" : university_student_result_string ,
        "university_courses" : university_courses_result_string ,
        "university_participate" : university_participate_result_string }

    print(f"Execute : {result_bool}")
    return jsonify(result)

@university_app.route('/drop_table_university_db', methods=['GET'])
def drop_table_university_db():
    """ DROP ALL TABLE IN THE DB """
    result_bool, resultString  = universityService.drop_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@university_app.route('/testGetUser', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = [{'last_name': user.last_name, 'first_name': user.first_name} for user in users]
    return jsonify({'users': users_list})