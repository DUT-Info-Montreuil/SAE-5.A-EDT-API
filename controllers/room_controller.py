from flask import Flask, jsonify
from flask import Blueprint

from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from contextlib import closing
from config import config

from services.room_service import room_service

room_app = Blueprint('room_app', __name__)

# Rooms API
# university.roles(@id, name, description, personal_id)
@room_app.route('/rooms/get', methods=['GET'])
def get_rooms():
    """ Get all rooms in JSON format """
    _service = room_service()
    returnStatement = _service.get_rooms()
    return jsonify(returnStatement)

@room_app.route('/rooms/get/<int:id>', methods=['GET'])
def get_room_by_id(id):
    """ Get a room by ID in JSON format """
    data = request.json
    _service = room_service()
    returnStatement = _service.get_room_by_id(id)
    return jsonify(returnStatement)

@room_app.route('/rooms/identify', methods=['POST'])
def identify_room():
    """Identify a room by code in JSON format"""
    data = request.json
    _service = room_service()
    returnStatement = _service.identify_room(data)
    return jsonify(returnStatement)

@room_app.route('/rooms/add', methods=['POST'])
def add_room():
    """ Add a room by data in JSON format """
    data = request.json
    _service = room_service()
    returnStatement = _service.add_room(data)

    if returnStatement:
        return jsonify({"message": "Room successfully added!"}), 200
    else:
        return jsonify({"message": "Room not found!"}), 404

@room_app.route('/rooms/delete/<int:id>', methods=['GET'])
def delete_room_by_id(id):
    """ Delete a room by ID in JSON format """
    _service = room_service()
    returnStatement = _service.delete_room_by_id(id)
    if returnStatement:
        return jsonify({"message": "Room deleted successfully!"}), 200
    else:
        return jsonify({"message": "Room not found!"}), 404

@room_app.route('/rooms/update/<int:id>', methods=['POST'])
def update_room(id):
    """ Update a room record by ID using data in JSON format """
    data = request.json
    _service = room_service()
    updated_room_id = _service.update_room(id, data)
    if updated_room_id:
        return {"message": f"Room record with ID {updated_room_id} updated successfully!"}, 200
    else:
        return {"message": f"Room record with ID {id} not found!"}, 404
