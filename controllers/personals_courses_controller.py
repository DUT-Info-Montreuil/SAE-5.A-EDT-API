from flask import jsonify
from flask import request
from flask import Blueprint

from services.personals_courses_service import personals_courses_service

personals_courses_app = Blueprint('personals_courses_app', __name__)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@personals_courses_app.route('/personals_courses/get', methods=['GET'])
def get_personals_courses():
    """ Get all personals_courses in JSON format """
    try:
        _service = personals_courses_service()
        returnStatement = _service.get_personals_courses()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404 

@personals_courses_app.route('/personals_courses/get/<int:id>', methods=['GET'])
def get_personals_courses_by_id(id):
    """ Get a personals_courses by ID in JSON format """
    try:
        data = request.json
        _service = personals_courses_service()
        returnStatement = _service.get_personals_courses_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404 

@personals_courses_app.route('/personals_courses/identify', methods=['POST'])
def identify_personals_courses():
    """Identify a personals_courses by code in JSON format"""
    try:
        data = request.json
        _service = personals_courses_service()
        returnStatement = _service.identify_rooms(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404 

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@personals_courses_app.route('/personals_courses/add', methods=['PUT'])
def add_personals_courses():
    """ Add a personals_courses by data in JSON format """
    try:
        data = request.json
        _service = personals_courses_service()
        _service.add_personals_courses(data)
        return jsonify({"message": "personals_courses successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@personals_courses_app.route('/personals_courses/delete/<int:id>', methods=['DELETE'])
def delete_personals_courses_by_id(id):
    """ Delete a personals_courses by ID in JSON format """
    try:
        _service = personals_courses_service()
        _service.delete_personals_courses_by_id(id)
        return jsonify({"message": "personals_courses successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@personals_courses_app.route('/personals_courses/update/<int:id>', methods=['PATCH'])
def update_personals_courses(id):
    """ Update a personals_courses record by ID using data in JSON format """
    try:
        data = request.json
        _service = personals_courses_service()
        _service.update_personals_courses(id, data)
        return jsonify({"message": "personals_courses successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
