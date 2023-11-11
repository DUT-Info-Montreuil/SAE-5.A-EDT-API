from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.reminder_service import reminder_service

reminder_app = Blueprint('reminder_app', __name__)


# Reminders API
# university.reminders(@id, #course_id, #subgroup_id)
@reminder_app.route('/reminders/get', methods=['GET'])
def get_reminders():
    """ Get all reminders in JSON format """
    _service = reminder_service()
    returnStatement = _service.get_reminders()
    return jsonify(returnStatement)

@reminder_app.route('/reminders/get/<int:id>', methods=['GET'])
def get_reminder_by_id(id):
    """ Get a reminder by ID in JSON format """
    _service = reminder_service()
    returnStatement = _service.get_reminder_by_id(id)
    return jsonify(returnStatement)

@reminder_app.route('/reminders/identify', methods=['POST'])
def identify_reminder():
    """Identify a reminder by course_id and subgroup_id in JSON format"""
    data = request.json
    _service = reminder_service()
    returnStatement = _service.identify_reminder(data)
    return jsonify(returnStatement)

@reminder_app.route('/reminders/add', methods=['POST'])
def add_reminder():
    """ Add a reminder by data in JSON format """
    data = request.json
    _service = reminder_service()
    returnStatement = _service.add_reminder(data)

    if returnStatement:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@reminder_app.route('/reminders/delete/<int:id>', methods=['GET'])
def delete_reminder_by_id(id):
    """ Delete a reminder by ID in JSON format """
    _service = reminder_service()
    returnStatement = _service.delete_reminder_by_id(id)
    if returnStatement:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404