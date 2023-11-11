from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.course_service import course_service

course_app = Blueprint('course_app', __name__)

# Courses API
# university.courses(@id, description, starttime, duree, course_type, #personal_id, #rooms_id, #teaching_id)
@course_app.route('/courses/get', methods=['GET'])
def get_courses():
    """ Get all courses in JSON format """
    _service = course_service()
    returnStatement = _service.get_courses()
    return jsonify(returnStatement)

@course_app.route('/courses/get/<int:id>', methods=['GET'])
def get_course_by_id(id):
    """ Get a course by ID in JSON format """
    _service = course_service()
    returnStatement = _service.get_course_by_id(id)
    return jsonify(returnStatement)

@course_app.route('/courses/identify', methods=['POST'])
def identify_course():
    """Identify a course by description, starttime, duree, course_type, personal_id, and rooms_id in JSON format"""
    data = request.json
    _service = course_service()
    returnStatement = _service.identify_course(data)
    return jsonify(returnStatement)

@course_app.route('/courses/add', methods=['POST'])
def add_course():
    """ Add a course by data in JSON format """
    data = request.json
    _service = course_service()
    returnStatement = _service.add_course(data)

    if returnStatement:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@course_app.route('/courses/delete/<int:id>', methods=['GET'])
def delete_course_by_id(id):
    """ Delete a course by ID in JSON format """
    _service = course_service()
    returnStatement = _service.delete_course_by_id(id)
    if returnStatement:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404