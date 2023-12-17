from flask import jsonify
from flask import request
from flask import Blueprint

from services.teaching_service import teaching_service

teaching_app = Blueprint('teaching_app', __name__)

# Teachings API
# university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@teaching_app.route('/teachings/get', methods=['GET'])
def get_teachings():
    """ Get all teachings in JSON format """
    _service = teaching_service()
    returnStatement = _service.get_teachings()
    return jsonify(returnStatement)

@teaching_app.route('/teachings/get/<int:id>', methods=['GET'])
def get_teaching_by_id(id):
    """ Get a teaching by ID in JSON format """
    _service = teaching_service()
    returnStatement = _service.get_teaching_by_id(id)
    return jsonify(returnStatement)

@teaching_app.route('/teachings/identify', methods=['POST'])
def identify_teaching():
    """Identify a teaching by title, hour_number, semestre, sequence, and specialization_id in JSON format"""
    data = request.json
    _service = teaching_service()
    returnStatement = _service.identify_teaching(data)
    return jsonify(returnStatement)

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@teaching_app.route('/teachings/add', methods=['PUT'])
def add_teaching():
    """ Add a teaching by data in JSON format """
    try:
        data = request.json
        _service = teaching_service()
        _service.add_teaching(data)
        return jsonify({"message": "Teaching successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@teaching_app.route('/teachings/delete/<int:id>', methods=['DELETE'])
def delete_teaching_by_id(id):
    """ Delete a teaching by ID in JSON format """
    _service = teaching_service()
    returnStatement = _service.delete_teaching_by_id(id)
    try:
        _service = teaching_service()
        _service.delete_teaching_by_id(id)
        return jsonify({"message": "Teaching successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

# Faire une requete patch
@teaching_app.route('/teachings/update/<int:id>', methods=['PATCH'])
def update_teaching(id):
    """ Update a teaching record by ID using data in JSON format """
    try:
        data = request.json
        _service = teaching_service()
        _service.update_teaching(id, data)
        return jsonify({"message": "Teaching successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404