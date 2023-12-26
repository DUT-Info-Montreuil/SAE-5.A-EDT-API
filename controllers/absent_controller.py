from flask import jsonify
from flask import request
from flask import Blueprint

from services.absent_service import absent_service

absent_app = Blueprint('absent_app', __name__)

# university.absents(@id, justified, student_number, #course_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@absent_app.route('/absents/get', methods=['GET'])
def get_absents():
    """ Get all absents in JSON format """
    try:
        _service = absent_service()
        returnStatement = _service.get_absents()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@absent_app.route('/absents/get/<int:id>', methods=['GET'])
def get_absent_by_id(id):
    """ Get an absent by ID in JSON format """
    try:
        _service = absent_service()
        returnStatement = _service.get_absent_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

# student_number and course_id needs to exists
# should add a constraint pour ne pas rendre absent des eleves qui ne participent pas à un cours
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