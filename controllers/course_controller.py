from flask import Blueprint, jsonify, request
from services.course_service import course_service

course_app = Blueprint('course_app', __name__)
courseService = course_service()

@course_app.route('/courses/get', methods=['GET'])
def get_courses():
    courses = courseService.get_all_courses()
    return jsonify({'courses': courses})

@course_app.route('/courses/get/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    course = courseService.get_course_by_id(course_id)

    if course:
        return jsonify({'course': course})
    else:
        return jsonify({'message': 'Course not found'}), 404

@course_app.route('/courses/identify', methods=['POST'])
def find_course():
    data = request.get_json()
    course = courseService.find_course(**data)

    if course:
        return jsonify({'course': course})
    else:
        return jsonify({'message': 'Course not found'}), 404
    
@course_app.route('/courses/update/<int:course_id>', methods=['PATCH'])
def update_course(course_id):
    data = request.get_json()
    success = courseService.update_course(course_id, data)

    if success:
        return jsonify({'message': 'Course updated successfully'})
    else:
        return jsonify({'message': 'Course not found'}), 404
    
@course_app.route('/courses/delete/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    success = courseService.delete_course(course_id)

    if success:
        return jsonify({'message': 'Course deleted successfully'})
    else:
        return jsonify({'message': 'Course not found'}), 404

@course_app.route('/courses/add', methods=['PUT'])
def add_course():
    
    data = request.json
    success = courseService.add_course(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Course not add'}), 404