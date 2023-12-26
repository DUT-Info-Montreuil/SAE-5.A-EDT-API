from flask import jsonify
from flask import request
from flask import Blueprint

from services.subgroup_service import subgroup_service

subgroup_app = Blueprint('subgroup_app', __name__)

# Subgroups API
# university.subgroups(@id, name, #group_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@subgroup_app.route('/subgroups/get', methods=['GET'])
def get_subgroups():
    """ Get all subgroups in JSON format """
    try:
        _service = subgroup_service()
        returnStatement = _service.get_subgroups()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


@subgroup_app.route('/subgroups/get/<int:id>', methods=['GET'])
def get_subgroup_by_id(id):
    """ Get a subgroup by ID in JSON format """
    try:
        _service = subgroup_service()
        returnStatement = _service.get_subgroup_by_id()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@subgroup_app.route('/subgroups/identify', methods=['POST'])
def identify_subgroup():
    """Identify a subgroup by name and group_id in JSON format"""
    try:
        data = request.json
        _service = subgroup_service()
        returnStatement = _service.identify_subgroup(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@subgroup_app.route('/subgroups/add', methods=['PUT'])
def add_subgroup():
    """ Add a subgroup by data in JSON format """
    try:
        data = request.json
        _service = subgroup_service()
        _service.add_subgroup(data)
        return jsonify({"message": "Subgroup successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@subgroup_app.route('/subgroups/delete/<int:id>', methods=['DELETE'])
def delete_subgroup_by_id(id):
    """ Delete a subgroup by ID in JSON format """
    try:
        _service = subgroup_service()
        _service.delete_subgroup_by_id(id)
        return jsonify({"message": "Subgroup successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@subgroup_app.route('/subgroups/update/<int:id>', methods=['PATCH'])
def update_subgroup(id):
    """ Update a subgroup record by ID using data in JSON format """
    try:
        data = request.json
        _service = subgroup_service()
        _service.update_subgroup(id, data)
        return jsonify({"message": "Subgroup successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
