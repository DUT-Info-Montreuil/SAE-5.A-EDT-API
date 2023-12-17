from flask import Blueprint, jsonify, request
from services.specialization_service import specialization_service

specialization_app = Blueprint('specialization_app', __name__)
specializationService = specialization_service()

@specialization_app.route('/specializations/get', methods=['GET'])
def get_specializations():
    specializations = specializationService.get_all_specializations()
    return jsonify({'specializations': specializations})

@specialization_app.route('/specializations/get/<int:specialization_id>', methods=['GET'])
def get_specialization_by_id(specialization_id):
    specialization = specializationService.get_specialization_by_id(specialization_id)

    if specialization:
        return jsonify({'specialization': specialization})
    else:
        return jsonify({'message': 'Specialization not found'}), 404

@specialization_app.route('/specializations/identify', methods=['POST'])
def find_specialization():
    data = request.get_json()
    specialization = specializationService.find_specialization(**data)

    if specialization:
        return jsonify({'specialization': specialization})
    else:
        return jsonify({'message': 'Specialization not found'}), 404
    
@specialization_app.route('/specializations/update/<int:specialization_id>', methods=['PATCH'])
def update_specialization(specialization_id):
    data = request.get_json()
    success = specializationService.update_specialization(specialization_id, data)

    if success:
        return jsonify({'message': 'Specialization updated successfully'})
    else:
        return jsonify({'message': 'Specialization not found'}), 404
    
@specialization_app.route('/specializations/delete/<int:specialization_id>', methods=['DELETE'])
def delete_specialization(specialization_id):
    success = specializationService.delete_specialization(specialization_id)

    if success:
        return jsonify({'message': 'Specialization deleted successfully'})
    else:
        return jsonify({'message': 'Specialization not found'}), 404

@specialization_app.route('/specializations/add', methods=['PUT'])
def add_specialization():
    
    data = request.json
    success = specializationService.add_specialization(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Specialization not add'}), 404