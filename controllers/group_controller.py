from flask import Blueprint, jsonify, request
from services.group_service import group_service

group_app = Blueprint('group_app', __name__)
groupService = group_service()

@group_app.route('/groups/get', methods=['GET'])
def get_groups():
    groups = groupService.get_all_groups()
    return jsonify({'groups': groups})

@group_app.route('/groups/get/<int:group_id>', methods=['GET'])
def get_group_by_id(group_id):
    group = groupService.get_group_by_id(group_id)

    if group:
        return jsonify({'group': group})
    else:
        return jsonify({'message': 'Group not found'}), 404

@group_app.route('/groups/identify', methods=['POST'])
def find_group():
    data = request.get_json()
    group = groupService.find_group(**data)

    if group:
        return jsonify({'group': group})
    else:
        return jsonify({'message': 'Group not found'}), 404
    
@group_app.route('/groups/update/<int:group_id>', methods=['PATCH'])
def update_group(group_id):
    data = request.get_json()
    success = groupService.update_group(group_id, data)

    if success:
        return jsonify({'message': 'Group updated successfully'})
    else:
        return jsonify({'message': 'Group not found'}), 404
    
@group_app.route('/groups/delete/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
    success = groupService.delete_group(group_id)

    if success:
        return jsonify({'message': 'Group deleted successfully'})
    else:
        return jsonify({'message': 'Group not found'}), 404

@group_app.route('/groups/add', methods=['PUT'])
def add_group():
    
    data = request.json
    success = groupService.add_group(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Group not add'}), 404