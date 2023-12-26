from flask import jsonify
from flask import request
from flask import Blueprint

from services.role_service import role_service

role_app = Blueprint('role_app', __name__)

# Roles API
# university.roles(@id, name, description, personal_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@role_app.route('/roles/get', methods=['GET'])
def get_roles():
    """ Get all roles in JSON format """
    try:
        _service = role_service()
        returnStatement = _service.get_roles()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@role_app.route('/roles/get/<int:id>', methods=['GET'])
def get_role_by_id(id):
    """ Get a role by ID in JSON format """
    try:
        _service = role_service()
        returnStatement = _service.get_role_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@role_app.route('/roles/identify', methods=['POST'])
def identify_role():
    """Identify a role by name, and personal_id in JSON format"""
    try:
        data = request.json
        _service = role_service()
        returnStatement = _service.identify_role(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@role_app.route('/roles/add', methods=['PUT'])
def add_role():
    """ Add a role by data in JSON format """
    try:
        data = request.json
        _service = role_service()
        _service.add_role(data)
        return jsonify({"message": "Role successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@role_app.route('/roles/delete/<int:id>', methods=['DELETE'])
def delete_role_by_id(id):
    """ Delete a role by ID in JSON format """
    try:
        _service = role_service()
        _service.delete_role_by_id(id)
        return jsonify({"message": "Role successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@role_app.route('/roles/update/<int:id>', methods=['PATCH'])
def update_role(id):
    """ Update a role record by ID using data in JSON format """
    try:
        data = request.json
        _service = role_service()
        _service.update_role(id, data)
        return jsonify({"message": "Role successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
