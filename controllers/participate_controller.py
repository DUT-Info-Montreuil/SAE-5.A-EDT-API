from flask import Blueprint, jsonify, request
from services.participate_service import participate_service

participate_app = Blueprint('participate_app', __name__)
participateService = participate_service()

@participate_app.route('/participates/get', methods=['GET'])
def get_participates():
    participates = participateService.get_all_participates()
    return jsonify({'participates': participates})

@participate_app.route('/participates/get/<int:participate_id>', methods=['GET'])
def get_participate_by_id(participate_id):
    participate = participateService.get_participate_by_id(participate_id)

    if participate:
        return jsonify({'participate': participate})
    else:
        return jsonify({'message': 'Participate not found'}), 404

@participate_app.route('/participates/identify', methods=['POST'])
def find_participate():
    data = request.get_json()
    participate = participateService.find_participate(**data)

    if participate:
        return jsonify({'participate': participate})
    else:
        return jsonify({'message': 'Participate not found'}), 404
    
@participate_app.route('/participates/update/<int:participate_id>', methods=['PATCH'])
def update_participate(participate_id):
    data = request.get_json()
    success = participateService.update_participate(participate_id, data)

    if success:
        return jsonify({'message': 'Participate updated successfully'})
    else:
        return jsonify({'message': 'Participate not found'}), 404
    
@participate_app.route('/participates/delete/<int:participate_id>', methods=['DELETE'])
def delete_participate(participate_id):
    success = participateService.delete_participate(participate_id)

    if success:
        return jsonify({'message': 'Participate deleted successfully'})
    else:
        return jsonify({'message': 'Participate not found'}), 404

@participate_app.route('/participates/add', methods=['PUT'])
def add_participate():
    
    data = request.json
    success = participateService.add_participate(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Participate not add'}), 404