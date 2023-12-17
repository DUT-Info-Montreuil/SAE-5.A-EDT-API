from flask import jsonify
from flask import request
from flask import Blueprint

from services.absent_service import absent_service

absent_app = Blueprint('absent_app', __name__)

# Absents API
# university.absents(@id, description, starttime, duree, absent_type, #personal_id, #rooms_id, #teaching_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@absent_app.route('/absents/get', methods=['GET'])
def get_absents():
    """ Get all absents in JSON format """
    _service = absent_service()
    returnStatement = _service.get_absents()
    return jsonify(returnStatement)

@absent_app.route('/absents/get/<int:id>', methods=['GET'])
def get_absent_by_id(id):
    """ Get a absent by ID in JSON format """
    _service = absent_service()
    returnStatement = _service.get_absent_by_id(id)
    return jsonify(returnStatement)

@absent_app.route('/absents/identify', methods=['POST'])
def identify_absent():
    """Identify a absent by description, starttime, duree, absent_type, personal_id, and rooms_id in JSON format"""
    data = request.json
    _service = absent_service()
    returnStatement = _service.identify_absent(data)
    return jsonify(returnStatement)


# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@absent_app.route('/absents/add', methods=['PUT'])
def add_absent():
    """ Add a absent by data in JSON format """
    try:
        data = request.json
        _service = absent_service()
        _service.add_absent(data)
        return jsonify({"message": "Absent successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@absent_app.route('/absents/delete/<int:id>', methods=['DELETE'])
def delete_absent_by_id(id):
    """ Delete a absent by ID in JSON format """
    try:
        _service = absent_service()
        _service.delete_absent_by_id(id)
        return jsonify({"message": "Absent successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@absent_app.route('/absent/update/<int:id>', methods=['PATCH'])
def update_absent(id):
    """ Update an absent record by ID using data in JSON format """
    try:
        data = request.json
        _service = absent_service()
        _service.update_absent(id, data)
        return jsonify({"message": "Absent successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404