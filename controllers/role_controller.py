from flask import Blueprint, jsonify, request

from services.role_service import role_service

role_app = Blueprint('role_app', __name__)

# Roles API
# university.roles(@id, name, description, personal_id)
@role_app.route('/roles/get', methods=['GET'])
def get_roles():
    """ Get all roles in JSON format """
    _service = role_service()
    returnStatement = _service.get_roles()
    return jsonify(returnStatement)

@role_app.route('/roles/get/<int:id>', methods=['GET'])
def get_role_by_id(id):
    """ Get a role by ID in JSON format """
    _service = role_service()
    returnStatement = _service.get_role_by_id(id)
    return jsonify(returnStatement)

@role_app.route('/roles/identify', methods=['POST'])
def identify_role():
    """Identify a role by name, and personal_id in JSON format"""
    data = request.json
    _service = role_service()
    returnStatement = _service.identify_role(data)
    return jsonify(returnStatement)

@role_app.route('/roles/add', methods=['POST'])
def add_role():
    """ Add a role by data in JSON format """
    data = request.json
    _service = role_service()
    returnStatement = _service.add_role(data)
    if returnStatement:
        return jsonify({"message": "Role successfully added!"}), 200
    else:
        return jsonify({"message": "Role not found!"}), 404

@role_app.route('/roles/delete/<int:id>', methods=['GET'])
def delete_role_by_id(id):
    """ Delete a role by ID in JSON format """
    _service = role_service()
    returnStatement = _service.delete_role_by_id(id)
    
    if returnStatement:
        return jsonify({"message": "Role deleted successfully!"}), 200
    else:
        return jsonify({"message": "Role not found!"}), 404

@role_app.route('/roles/update/<int:id>', methods=['POST'])
def update_role(id):
    """ Update a role record by ID using data in JSON format """
    data = request.json
    _service = role_service()
    updated_role_id = _service.update_role(id, data)
    if updated_role_id:
        return {"message": f"Role record with ID {updated_role_id} updated successfully!"}, 200
    else:
        return {"message": f"Role record with ID {id} not found!"}, 404
