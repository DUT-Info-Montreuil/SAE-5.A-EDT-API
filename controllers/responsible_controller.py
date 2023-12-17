from flask import Blueprint, jsonify, request
from services.responsible_service import responsible_service

responsible_app = Blueprint('responsible_app', __name__)
responsibleService = responsible_service()

@responsible_app.route('/responsibles/get', methods=['GET'])
def get_responsibles():
    responsibles = responsibleService.get_all_responsibles()
    return jsonify({'responsibles': responsibles})

@responsible_app.route('/responsibles/get/<int:responsible_id>', methods=['GET'])
def get_responsible_by_id(responsible_id):
    responsible = responsibleService.get_responsible_by_id(responsible_id)

    if responsible:
        return jsonify({'responsible': responsible})
    else:
        return jsonify({'message': 'Responsible not found'}), 404

@responsible_app.route('/responsibles/identify', methods=['POST'])
def find_responsible():
    data = request.get_json()
    responsible = responsibleService.find_responsible(**data)

    if responsible:
        return jsonify({'responsible': responsible})
    else:
        return jsonify({'message': 'Responsible not found'}), 404
    
@responsible_app.route('/responsibles/update/<int:responsible_id>', methods=['PATCH'])
def update_responsible(responsible_id):
    data = request.get_json()
    success = responsibleService.update_responsible(responsible_id, data)

    if success:
        return jsonify({'message': 'Responsible updated successfully'})
    else:
        return jsonify({'message': 'Responsible not found'}), 404
    
@responsible_app.route('/responsibles/delete/<int:responsible_id>', methods=['DELETE'])
def delete_responsible(responsible_id):
    success = responsibleService.delete_responsible(responsible_id)

    if success:
        return jsonify({'message': 'Responsible deleted successfully'})
    else:
        return jsonify({'message': 'Responsible not found'}), 404

@responsible_app.route('/responsibles/add', methods=['PUT'])
def add_responsible():
    
    data = request.json
    success = responsibleService.add_responsible(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Responsible not add'}), 404