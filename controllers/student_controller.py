from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.student_service import student_service

student_app = Blueprint('student_app', __name__)

# Students API
# university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
@student_app.route('/students/get', methods=['GET'])
def get_students():
    """ Get all students in JSON format """
    _service = student_service()
    returnStatement = _service.get_students()
    return jsonify(returnStatement)

@student_app.route('/students/get/<string:student_number>', methods=['GET'])
def get_student_by_student_number(student_number):
    """ Get a student by student_number in JSON format """
    
    _service = student_service()
    returnStatement = _service.get_student_by_student_number(student_number)
    return jsonify(returnStatement)

@student_app.route('/students/identify', methods=['POST'])
def identify_student():
    """Identify a student by last_name, first_name, mail, phone_number, department_id, group_id and subgroup_id in JSON format"""
    
    data = request.json
    _service = student_service()
    returnStatement = _service.identify_student(data)
    return jsonify(returnStatement)

@student_app.route('/students/add', methods=['POST'])
def add_student():
    """ Add a student by data in JSON format """

    data = request.json
    _service = student_service()
    returnStatement = _service.add_student(data)
    if returnStatement:
        return jsonify({"message": "Student successfully added!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

@student_app.route('/students/delete/<string:student_number>', methods=['GET'])
def delete_student_by_id(student_number):
    """ Delete a student by ID in JSON format """
    _service = student_service()
    returnStatement = _service.delete_student_by_id(id)
    if returnStatement:
        return jsonify({"message": "Student deleted successfully!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

@student_app.route('/students/update/<string:student_number>', methods=['POST'])
def update_student(student_number):
    """ Update a student record by student_number using data in JSON format """
    data = request.json
    _service = student_service()
    updated_student_number = _service.update_student(student_number, data)
    if updated_student_number:
        return {"message": f"Student record with student number {updated_student_number} updated successfully!"}, 200
    else:
        return {"message": f"Student record with student number {student_number} not found!"}, 404
