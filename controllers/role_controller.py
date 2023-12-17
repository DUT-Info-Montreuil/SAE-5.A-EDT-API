from flask import Blueprint, jsonify, request
from services.role_service import role_service

role_app = Blueprint('role_app', __name__)
roleService = role_service()

@role_app.route('/roles/get', methods=['GET'])
def get_roles():
    roles = roleService.get_all_roles()
    return jsonify({'roles': roles})

@role_app.route('/roles/get/<int:role_id>', methods=['GET'])
def get_role_by_id(role_id):
    role = roleService.get_role_by_id(role_id)

    if role:
        return jsonify({'role': role})
    else:
        return jsonify({'message': 'Role not found'}), 404

@role_app.route('/roles/identify', methods=['POST'])
def find_role():
    data = request.get_json()
    role = roleService.find_role(**data)

    if role:
        return jsonify({'role': role})
    else:
        return jsonify({'message': 'Role not found'}), 404
    
@role_app.route('/roles/update/<int:role_id>', methods=['PATCH'])
def update_role(role_id):
    data = request.get_json()
    success = roleService.update_role(role_id, data)

    if success:
        return jsonify({'message': 'Role updated successfully'})
    else:
        return jsonify({'message': 'Role not found'}), 404
    
@role_app.route('/roles/delete/<int:role_id>', methods=['DELETE'])
def delete_role(role_id):
    success = roleService.delete_role(role_id)

    if success:
        return jsonify({'message': 'Role deleted successfully'})
    else:
        return jsonify({'message': 'Role not found'}), 404

@role_app.route('/roles/add', methods=['PUT'])
def add_role():
    
    data = request.json
    success = roleService.add_role(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Role not add'}), 404