from flask import Blueprint, jsonify, request
from services.room_service import room_service

room_app = Blueprint('room_app', __name__)
roomService = room_service()

@room_app.route('/rooms/get', methods=['GET'])
def get_rooms():
    rooms = roomService.get_all_rooms()
    return jsonify({'rooms': rooms})

@room_app.route('/rooms/get/<int:room_id>', methods=['GET'])
def get_room_by_id(room_id):
    room = roomService.get_room_by_id(room_id)

    if room:
        return jsonify({'room': room})
    else:
        return jsonify({'message': 'Room not found'}), 404

@room_app.route('/rooms/identify', methods=['POST'])
def find_room():
    data = request.get_json()
    room = roomService.find_room(**data)

    if room:
        return jsonify({'room': room})
    else:
        return jsonify({'message': 'Room not found'}), 404
    
@room_app.route('/rooms/update/<int:room_id>', methods=['PATCH'])
def update_room(room_id):
    data = request.get_json()
    success = roomService.update_room(room_id, data)

    if success:
        return jsonify({'message': 'Room updated successfully'})
    else:
        return jsonify({'message': 'Room not found'}), 404
    
@room_app.route('/rooms/delete/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    success = roomService.delete_room(room_id)

    if success:
        return jsonify({'message': 'Room deleted successfully'})
    else:
        return jsonify({'message': 'Room not found'}), 404

@room_app.route('/rooms/add', methods=['PUT'])
def add_room():
    
    data = request.json
    success = roomService.add_room(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Room not add'}), 404