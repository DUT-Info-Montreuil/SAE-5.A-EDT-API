from flask import Blueprint, jsonify, request
from services.department_service import department_service

department_app = Blueprint('department_app', __name__)
departmentService = department_service()

@department_app.route('/departments/get', methods=['GET'])
def get_departments():
    departments = departmentService.get_all_departments()
    return jsonify({'departments': departments})

@department_app.route('/departments/get/<int:department_id>', methods=['GET'])
def get_department_by_id(department_id):
    department = departmentService.get_department_by_id(department_id)

    if department:
        return jsonify({'department': department})
    else:
        return jsonify({'message': 'Department not found'}), 404

@department_app.route('/departments/identify', methods=['POST'])
def find_department():
    data = request.get_json()
    department = departmentService.find_department(**data)

    if department:
        return jsonify({'department': department})
    else:
        return jsonify({'message': 'Department not found'}), 404
    
@department_app.route('/departments/update/<int:department_id>', methods=['PATCH'])
def update_department(department_id):
    data = request.get_json()
    success = departmentService.update_department(department_id, data)

    if success:
        return jsonify({'message': 'Department updated successfully'})
    else:
        return jsonify({'message': 'Department not found'}), 404
    
@department_app.route('/departments/delete/<int:department_id>', methods=['DELETE'])
def delete_department(department_id):
    success = departmentService.delete_department(department_id)

    if success:
        return jsonify({'message': 'Department deleted successfully'})
    else:
        return jsonify({'message': 'Department not found'}), 404

@department_app.route('/departments/add', methods=['PUT'])
def add_department():
    
    data = request.json
    success = departmentService.add_department(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Department not add'}), 404