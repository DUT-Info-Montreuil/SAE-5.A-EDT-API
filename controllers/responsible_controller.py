from flask import jsonify
from flask import request
from flask import Blueprint

from services.responsible_service import responsible_service

responsible_app = Blueprint('responsible_app', __name__)

# Responsibles API
# university.responsibles(@id, #personal_id, #teaching_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@responsible_app.route('/responsibles/get', methods=['GET'])
def get_responsibles():
    """ Get all responsibles in JSON format """
    try:
        _service = responsible_service()
        returnStatement = _service.get_responsibles()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@responsible_app.route('/responsibles/get/<int:id>', methods=['GET'])
def get_responsible_by_id(id):
    """ Get a responsible by ID in JSON format """
    try:
        _service = responsible_service()
        returnStatement = _service.get_responsible_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@responsible_app.route('/responsibles/identify', methods=['POST'])
def identify_responsible():
    """Identify a responsible by course_id and subgroup_id in JSON format"""
    try:
        data = request.json
        _service = responsible_service()
        returnStatement = _service.identify_responsible(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@responsible_app.route('/responsibles/add', methods=['PUT'])
def add_responsible():
    """ Add a responsible by data in JSON format """
    try:
        data = request.json
        _service = responsible_service()
        _service.add_responsible(data)
        return jsonify({"message": "Responsible successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@responsible_app.route('/responsibles/delete/<int:id>', methods=['DELETE'])
def delete_responsible_by_id(id):
    """ Delete a responsible by ID in JSON format """
    try:
        _service = responsible_service()
        _service.delete_responsible_by_id(id)
        return jsonify({"message": "Responsible successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@responsible_app.route('/responsibles/update/<int:id>', methods=['PATCH'])
def update_responsible(id):
    """ Update a responsible record by ID using data in JSON format """
    try:
        data = request.json
        _service = responsible_service()
        _service.update_responsible(id, data)
        return jsonify({"message": "Responsible successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404