from flask import Blueprint, jsonify, request
from services.personal_service import personal_service

personal_app = Blueprint('personal_app', __name__)
personalService = personal_service()

@personal_app.route('/personals/get', methods=['GET'])
def get_personals():
    personals = personalService.get_all_personals()
    return jsonify({'personals': personals})

@personal_app.route('/personals/get/<int:personal_id>', methods=['GET'])
def get_personal_by_id(personal_id):
    personal = personalService.get_personal_by_id(personal_id)

    if personal:
        return jsonify({'personal': personal})
    else:
        return jsonify({'message': 'Personal not found'}), 404

@personal_app.route('/personals/identify', methods=['POST'])
def find_personal():
    data = request.get_json()
    personal = personalService.find_personal(**data)

    if personal:
        return jsonify({'personal': personal})
    else:
        return jsonify({'message': 'Personal not found'}), 404
    
@personal_app.route('/personals/update/<int:personal_id>', methods=['PATCH'])
def update_personal(personal_id):
    data = request.get_json()
    success = personalService.update_personal(personal_id, data)

    if success:
        return jsonify({'message': 'Personal updated successfully'})
    else:
        return jsonify({'message': 'Personal not found'}), 404
    
@personal_app.route('/personals/delete/<int:personal_id>', methods=['DELETE'])
def delete_personal(personal_id):
    success = personalService.delete_personal(personal_id)

    if success:
        return jsonify({'message': 'Personal deleted successfully'})
    else:
        return jsonify({'message': 'Personal not found'}), 404

@personal_app.route('/personals/add', methods=['PUT'])
def add_personal():
    
    data = request.json
    success = personalService.add_personal(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Personal not add'}), 404