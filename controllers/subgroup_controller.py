from flask import Blueprint, jsonify, request
from services.subgroup_service import subgroup_service

subgroup_app = Blueprint('subgroup_app', __name__)
subgroupService = subgroup_service()

@subgroup_app.route('/subgroups/get', methods=['GET'])
def get_subgroups():
    subgroups = subgroupService.get_all_subgroups()
    return jsonify({'subgroups': subgroups})

@subgroup_app.route('/subgroups/get/<int:subgroup_id>', methods=['GET'])
def get_subgroup_by_id(subgroup_id):
    subgroup = subgroupService.get_subgroup_by_id(subgroup_id)

    if subgroup:
        return jsonify({'subgroup': subgroup})
    else:
        return jsonify({'message': 'Subgroup not found'}), 404

@subgroup_app.route('/subgroups/identify', methods=['POST'])
def find_subgroup():
    data = request.get_json()
    subgroup = subgroupService.find_subgroup(**data)

    if subgroup:
        return jsonify({'subgroup': subgroup})
    else:
        return jsonify({'message': 'Subgroup not found'}), 404
    
@subgroup_app.route('/subgroups/update/<int:subgroup_id>', methods=['PATCH'])
def update_subgroup(subgroup_id):
    data = request.get_json()
    success = subgroupService.update_subgroup(subgroup_id, data)

    if success:
        return jsonify({'message': 'Subgroup updated successfully'})
    else:
        return jsonify({'message': 'Subgroup not found'}), 404
    
@subgroup_app.route('/subgroups/delete/<int:subgroup_id>', methods=['DELETE'])
def delete_subgroup(subgroup_id):
    success = subgroupService.delete_subgroup(subgroup_id)

    if success:
        return jsonify({'message': 'Subgroup deleted successfully'})
    else:
        return jsonify({'message': 'Subgroup not found'}), 404

@subgroup_app.route('/subgroups/add', methods=['PUT'])
def add_subgroup():
    
    data = request.json
    success = subgroupService.add_subgroup(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Subgroup not add'}), 404