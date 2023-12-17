from flask import Blueprint, jsonify, request
from services.absent_service import absent_service

absent_app = Blueprint('absent_app', __name__)
absentService = absent_service()

@absent_app.route('/absents/get', methods=['GET'])
def get_absents():
    absents = absentService.get_all_absents()
    return jsonify({'absents': absents})

@absent_app.route('/absents/get/<int:absent_id>', methods=['GET'])
def get_absent_by_id(absent_id):
    absent = absentService.get_absent_by_id(absent_id)

    if absent:
        return jsonify({'absent': absent})
    else:
        return jsonify({'message': 'Absent not found'}), 404

@absent_app.route('/absents/identify', methods=['POST'])
def find_absent():
    data = request.get_json()
    absent = absentService.find_absent(**data)

    if absent:
        return jsonify({'absent': absent})
    else:
        return jsonify({'message': 'Absent not found'}), 404
    
@absent_app.route('/absents/update/<int:absent_id>', methods=['PATCH'])
def update_absent(absent_id):
    data = request.get_json()
    success = absentService.update_absent(absent_id, data)

    if success:
        return jsonify({'message': 'Absent updated successfully'})
    else:
        return jsonify({'message': 'Absent not found'}), 404
    
@absent_app.route('/absents/delete/<int:absent_id>', methods=['DELETE'])
def delete_absent(absent_id):
    success = absentService.delete_absent(absent_id)

    if success:
        return jsonify({'message': 'Absent deleted successfully'})
    else:
        return jsonify({'message': 'Absent not found'}), 404

@absent_app.route('/absents/add', methods=['PUT'])
def add_absent():
    
    data = request.json
    success = absentService.add_absent(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Absent not add'}), 404