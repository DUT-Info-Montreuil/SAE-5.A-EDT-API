from flask import jsonify
from flask import request
from flask import Blueprint

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

# ----------------------------------------------------------
# Recuperer timetable
# ----------------------------------------------------------

@course_app.route('/courses/timetable/by-room', methods=['POST'])
#@jwt_required()
def get_timetable_by_room():
    """ Get timetable by group"""
    try:
        data = request.json
        _service = course_service()
        returnStatement = _service.get_timetable_by_room(data)
        return jsonify({'edt' : returnStatement})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@course_app.route('/courses/timetable/by-teacher', methods=['POST'])
#@jwt_required()   
def get_timetable_by_teacher():
    """ Get timetable by teacher_id"""
    try:    
        data = request.json
        _service = course_service()
        returnStatement = _service.get_timetable_by_teacher(data)
        return jsonify({'edt' : returnStatement})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@course_app.route('/courses/timetable/by-department-and-promotion', methods=['POST'])
#@jwt_required()   
def get_timetable_by_department():
    """ Get timetable by teacher_id"""  
    try:
        data = request.json
        _service = course_service()
        returnStatement = _service.get_timetable_by_department(data)
        return jsonify({'edt' : returnStatement})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@course_app.route('/courses/timetable/by-student', methods=['POST'])
#@jwt_required()   
def get_timetable_by_student():
    """ Get timetable by teacher_id"""
    try:
        data = request.json
        _service = course_service()
        returnStatement = _service.get_timetable_by_student(data)
        return jsonify({'edt' : returnStatement})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
# Identifier si user = prof ou student
# @ to-do
# @timetable_app.route('/timetable/get/bytoken', methods=['POST'])
# @jwt_required()
# def get_timetable_by_token():
#     return jsonify(get_jwt_identity())

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@course_app.route('/courses/add', methods=['PUT'])
def add_course():
    """ Add a course by data in JSON format """
    try:
        data = request.json
        _service = course_service()
        _service.add_course(data)
        return jsonify({"message": "Course successfully added!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@course_app.route('/courses/delete/<int:id>', methods=['DELETE'])
@course_app.route('/courses/delete/<int:id>', methods=['DELETE'])
def delete_course_by_id(id):
    """ Delete a course by ID in JSON format """
    try:
        _service = course_service()
        _service.delete_course_by_id(id)
        return jsonify({"message": "Course successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@course_app.route('/courses/update/<int:id>', methods=['PATCH'])
def update_course(id):
    """ Update a course by ID using data in JSON format """
    try:
        data = request.json
        _service = course_service()
        _service.update_course(id, data)
        return jsonify({"message": "Course successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


