from flask import jsonify
from flask import request
from flask import Blueprint

from services.rooms_courses_service import rooms_courses_service

rooms_courses_app = Blueprint('rooms_courses_app', __name__)

# rooms API
# university.roles(@id, name, description, personal_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@rooms_courses_app.route('/roomscourses/get', methods=['GET'])
def get_rooms_courses():
    """ Get all rooms_courses in JSON format """
    try:
        _service = rooms_courses_service()
        returnStatement = _service.get_rooms_courses()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404 

@rooms_courses_app.route('/rooms_courses/get/<int:id>', methods=['GET'])
def get_rooms_courses_by_id(id):
    """ Get a rooms_courses by ID in JSON format """
    data = request.json
    _service = rooms_courses_service()
    returnStatement = _service.get_rooms_courses_by_id(id)
    return jsonify(returnStatement)

@rooms_courses_app.route('/rooms_courses/identify', methods=['POST'])
def identify_rooms_courses():
    """Identify a rooms_courses by code in JSON format"""
    data = request.json
    _service = rooms_courses_service()
    returnStatement = _service.identify_rooms(data)
    return jsonify(returnStatement)

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@rooms_courses_app.route('/rooms_courses/add', methods=['PUT'])
def add_rooms_courses():
    """ Add a rooms_courses by data in JSON format """
    try:
        data = request.json
        _service = rooms_courses_service()
        _service.add_rooms_courses(data)
        return jsonify({"message": "rooms_courses successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@rooms_courses_app.route('/rooms_courses/delete/<int:id>', methods=['DELETE'])
def delete_rooms_courses_by_id(id):
    """ Delete a rooms_courses by ID in JSON format """
    try:
        _service = rooms_courses_service()
        _service.delete_rooms_courses_by_id(id)
        return jsonify({"message": "rooms_courses successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@rooms_courses_app.route('/rooms_courses/update/<int:id>', methods=['PATCH'])
def update_rooms_courses(id):
    """ Update a rooms_courses record by ID using data in JSON format """
    try:
        data = request.json
        _service = rooms_courses_service()
        _service.update_rooms_courses(id, data)
        return jsonify({"message": "rooms_courses successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
