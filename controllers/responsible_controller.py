from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.responsible_service import responsible_service

responsible_app = Blueprint('responsible_app', __name__)

# Responsibles API
# university.responsibles(@id, #personal_id, #teaching_id)
@responsible_app.route('/responsibles/get', methods=['GET'])
def get_responsibles():
    """ Get all responsibles in JSON format """
    _service = responsible_service()
    returnStatement = _service.get_responsibles()
    return jsonify([obj.jsonify() for obj in returnStatement])

@responsible_app.route('/responsibles/get/<int:id>', methods=['GET'])
def get_responsible_by_id(id):
    """ Get a responsible by ID in JSON format """
    _service = responsible_service()
    returnStatement = _service.get_responsible_by_id(id)
    return jsonify([obj.jsonify() for obj in returnStatement])

@responsible_app.route('/responsibles/identify', methods=['POST'])
def identify_responsible():
    """Identify a responsible by course_id and subgroup_id in JSON format"""
    data = request.json
    _service = responsible_service()
    returnStatement = _service.identify_responsible(data)
    return jsonify([obj.jsonify() for obj in returnStatement])

@responsible_app.route('/responsibles/add', methods=['POST'])
def add_responsible():
    """ Add a responsible by data in JSON format """
    data = request.json
    _service = responsible_service()
    returnStatement = _service.add_responsible(data)

    if returnStatement:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@responsible_app.route('/responsibles/delete/<int:id>', methods=['GET'])
def delete_responsible_by_id(id):
    """ Delete a responsible by ID in JSON format """
    _service = responsible_service()
    returnStatement = _service.delete_responsible_by_id(id)
    if returnStatement:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@responsible_app.route('/responsibles/update/<int:id>', methods=['POST'])
def update_responsible(id):
    """ Update a responsible record by ID using data in JSON format """
    data = request.json
    _service = responsible_service()
    updated_responsible_id = _service.update_responsible(id, data)
    if updated_responsible_id:
        return {"message": f"Responsible record with ID {updated_responsible_id} updated successfully!"}, 200
    else:
        return {"message": f"Responsible record with ID {id} not found!"}, 404
