from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.teaching_service import teaching_service

teaching_app = Blueprint('teaching_app', __name__)

# Teachings API
# university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
@teaching_app.route('/teachings/get', methods=['GET'])
def get_teachings():
    """ Get all teachings in JSON format """
    _service = teaching_service()
    returnStatement = _service.get_teachings()
    return jsonify(returnStatement)

@teaching_app.route('/teachings/get/<int:id>', methods=['GET'])
def get_teaching_by_id(id):
    """ Get a teaching by ID in JSON format """
    _service = teaching_service()
    returnStatement = _service.get_teaching_by_id(id)
    return jsonify(returnStatement)

@teaching_app.route('/teachings/identify', methods=['POST'])
def identify_teaching():
    """Identify a teaching by title, hour_number, semestre, sequence, and specialization_id in JSON format"""
    data = request.json
    _service = teaching_service()
    returnStatement = _service.identify_teaching(data)
    return jsonify(returnStatement)

@teaching_app.route('/teachings/add', methods=['POST'])
def add_teaching():
    """ Add a teaching by data in JSON format """
    data = request.json
    _service = teaching_service()
    returnStatement = _service.add_teaching(data)
    if returnStatement:
        return jsonify({"message": "Teaching successfully added!"}), 200
    else:
        return jsonify({"message": "Teaching not found!"}), 404

@teaching_app.route('/teachings/delete/<int:id>', methods=['GET'])
def delete_teaching_by_id(id):
    """ Delete a teaching by ID in JSON format """
    _service = teaching_service()
    returnStatement = _service.delete_teaching_by_id(id)
    if returnStatement:
        return jsonify({"message": "Teaching deleted successfully!"}), 200
    else:
        return jsonify({"message": "Teaching not found!"}), 404