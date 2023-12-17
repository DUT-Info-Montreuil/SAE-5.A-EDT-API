from flask import Blueprint, jsonify, request
from services.student_service import student_service

student_app = Blueprint('student_app', __name__)
studentService = student_service()

@student_app.route('/students/get', methods=['GET'])
def get_students():
    students = studentService.get_all_students()
    return jsonify({'students': students})

@student_app.route('/students/get/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = studentService.get_student_by_id(student_id)

    if student:
        return jsonify({'student': student})
    else:
        return jsonify({'message': 'Student not found'}), 404

@student_app.route('/students/identify', methods=['POST'])
def find_student():
    data = request.get_json()
    student = studentService.find_student(**data)

    if student:
        return jsonify({'student': student})
    else:
        return jsonify({'message': 'Student not found'}), 404
    
@student_app.route('/students/update/<int:student_id>', methods=['PATCH'])
def update_student(student_id):
    data = request.get_json()
    success = studentService.update_student(student_id, data)

    if success:
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'message': 'Student not found'}), 404
    
@student_app.route('/students/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    success = studentService.delete_student(student_id)

    if success:
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'message': 'Student not found'}), 404

@student_app.route('/students/add', methods=['PUT'])
def add_student():
    
    data = request.json
    success = studentService.add_student(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Student not add'}), 404