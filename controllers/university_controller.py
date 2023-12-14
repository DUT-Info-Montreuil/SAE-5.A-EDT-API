#!/usr/bin/env python
# -*- coding: utf-8 -*-

from services.sql_alchemy_service import *
from flask import jsonify, request, Blueprint, render_template, request
from flask_jwt_extended import get_jwt_identity, jwt_required

university_app = Blueprint('university_app', __name__)


@university_app.route('/create_university_db', methods=['GET'])
def create_university_db():
    """!! Warning this methode drop all before !!  CREATE ALL DB this methode will DROP all BEFORE create """
    from services.university_service import university_service
    _service = university_service()
    result_bool, resultString  = _service.initialize_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)

@university_app.route('/create_table_university_db', methods=['GET'])
def create_table_university_db():
    """ DROP AND CREATE ALL TABLE IN DB """
    from services.university_service import university_service
    _service = university_service()
    result_bool, resultString  = _service.create_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString) 

@university_app.route('/insert_table_university_db', methods=['GET'])
def insert_table_university_db():
    """ INSERT IN ALL TABLE IN THE DB """
    from services.university_service import university_service
    _service = university_service()
    university_user_result_bool, university_user_result_string  = _service.insert_university_user()
    university_school_result_bool, university_school_result_string  = _service.insert_university_school()
    university_student_result_bool, university_student_result_string  = _service.insert_university_student()
    university_courses_result_bool, university_courses_result_string  = _service.insert_university_courses()
    university_participate_result_bool, university_participate_result_string  = _service.insert_university_participate()
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
    from services.university_service import university_service
    _service = university_service()
    result_bool, resultString  = _service.drop_database()
    print(f"Execute : {result_bool}")
    return jsonify(resultString)


@university_app.route('/test', methods=['GET'])
def get_all_users():
    from services.university_service import university_service
    from entities.models.models import Student
    users = Student.query.all()
    users_list = [{'last_name': user.last_name, 'first_name': user.first_name} for user in users]

    return jsonify({'users': users_list})