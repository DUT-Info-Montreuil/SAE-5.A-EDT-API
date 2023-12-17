from flask import Blueprint, jsonify, request

from services.course_service import course_service

course_app = Blueprint('course_app', __name__)

# university.courses(@id, description, starttime, endtime, course_type, #personal_id, #rooms_id, #teaching_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@course_app.route('/courses/get', methods=['GET'])
def get_courses():
    """ Get all courses in JSON format """
    _service = course_service()
    returnStatement = _service.get_courses()
    return jsonify(returnStatement)

@course_app.route('/courses/get/<int:id>', methods=['GET'])
def get_course_by_id(id):
    """ Get a course by ID in JSON format """
    _service = course_service()
    returnStatement = _service.get_course_by_id(id)
    return jsonify(returnStatement)

@course_app.route('/courses/hours-by-teachers/get/<int:id>', methods=['GET'])
def identify_course(id):
    """Get number of hours of a teacher in JSON format"""
    _service = course_service()
    returnStatement = _service.identify_course(id)
    return jsonify(returnStatement)

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@course_app.route('/courses/add', methods=['PUT'])
def add_course():
    """ Add a course by data in JSON format """
    data = request.json
    _service = course_service()
    returnStatement = _service.add_course(data)

    if returnStatement:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@course_app.route('/courses/delete/<int:id>', methods=['GET'])
def delete_course_by_id(id):
    """ Delete a course by ID in JSON format """
    _service = course_service()
    returnStatement = _service.delete_course_by_id(id)
    if returnStatement:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404
    
@course_app.route('/courses/update/<int:id>', methods=['PATCH'])
def update_course(id):
    """ Update a course by ID using data in JSON format """
    data = request.json
    _service = course_service()
    return _service.update_course(id, data)

