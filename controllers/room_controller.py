from flask import jsonify
from flask import request
from flask import Blueprint

from services.room_service import room_service

room_app = Blueprint('room_app', __name__)

# Rooms API
# university.roles(@id, name, description, personal_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

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

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@room_app.route('/rooms/add', methods=['PUT'])
def add_room():
    """ Add a room by data in JSON format """
    try:
        data = request.json
        _service = room_service()
        _service.add_room(data)
        return jsonify({"message": "Room successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@room_app.route('/rooms/delete/<int:id>', methods=['DELETE'])
def delete_room_by_id(id):
    """ Delete a room by ID in JSON format """
    try:
        _service = room_service()
        _service.delete_room_by_id(id)
        return jsonify({"message": "Room successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@room_app.route('/rooms/update/<int:id>', methods=['PATCH'])
def update_room(id):
    """ Update a room record by ID using data in JSON format """
    try:
        data = request.json
        _service = room_service()
        _service.update_room(id, data)
        return jsonify({"message": "Room successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
