from flask import jsonify
from flask import request
from flask import Blueprint

from services.group_service import group_service

group_app = Blueprint('group_app', __name__)

# Groups API
# university.groups(@id, promotion, type, #department_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@group_app.route('/groups/get', methods=['GET'])
def get_groups():
    """ Get all groups in JSON format """
    try:
        _service = group_service()
        returnStatement = _service.get_groups()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@group_app.route('/groups/get/<int:id>', methods=['GET'])
def get_group_by_id(id):
    """ Get a group by ID in JSON format """
    try:
        _service = group_service()
        returnStatement = _service.get_group_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@group_app.route('/groups/identify', methods=['POST'])
def identify_group():
    """Identify a group by promotion and type in JSON format"""
    try:
        data = request.json
        _service = group_service()
        returnStatement = _service.identify_group(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@group_app.route('/groups/add', methods=['PUT'])
def add_group():
    """ Add a group by data in JSON format """
    try:
        data = request.json
        _service = group_service()
        _service.add_group(data)
        return jsonify({"message": "Group successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 404

@group_app.route('/groups/delete/<int:id>', methods=['DELETE'])
def delete_group_by_id(id):
    """ Delete a group by ID in JSON format """
    try:
        _service = group_service()
        _service.delete_group_by_id(id)
        return jsonify({"message": "Group successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 404
    
@group_app.route('/groups/update/<int:id>', methods=['PATCH'])
def update_group(id):
    """ Update a group record by ID using data in JSON format """
    try:
        data = request.json
        _service = group_service()
        _service.update_group(id, data)
        return jsonify({"message": "Group successfully updated!"}), 200

    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 404
