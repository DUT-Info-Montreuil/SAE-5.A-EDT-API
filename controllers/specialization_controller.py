from flask import jsonify
from flask import request
from flask import Blueprint

from services.specialization_service import specialization_service

specialization_app = Blueprint('specialization_app', __name__)


# Specializations API
# university.specializations(@id, code, name, #department_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@specialization_app.route('/specializations/get', methods=['GET'])
def get_specializations():
    """ Get all specializations in JSON format """
    try:
        _service = specialization_service()
        returnStatement = _service.get_specializations()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@specialization_app.route('/specializations/get/<int:id>', methods=['GET'])
def get_specialization_by_id(id):
    """ Get a specialization by ID in JSON format """
    try:
        _service = specialization_service()
        returnStatement = _service.get_specialization_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@specialization_app.route('/specializations/identify', methods=['POST'])
def identify_specialization():
    """Identify a specialization by code in JSON format"""
    try:
        data = request.json
        _service = specialization_service()
        returnStatement = _service.identify_specialization(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@specialization_app.route('/specializations/add', methods=['PUT'])
def add_specialization():
    """ Add a specialization by data in JSON format """
    try:
        data = request.json
        _service = specialization_service()
        _service.add_specialization(data)
        return jsonify({"message": "Specialization successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@specialization_app.route('/specializations/delete/<int:id>', methods=['DELETE'])
def delete_specialization_by_id(id):
    """ Delete a specialization by ID in JSON format """
    try:
        _service = specialization_service()
        _service.delete_specialization_by_id(id)
        return jsonify({"message": "Specialization successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@specialization_app.route('/specializations/update/<int:id>', methods=['PATCH'])
def update_specialization(id):
    """ Update a specialization record by ID using data in JSON format """
    try:
        data = request.json
        _service = specialization_service()
        _service.update_specialization(id, data)
        return jsonify({"message": "Specialization successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404