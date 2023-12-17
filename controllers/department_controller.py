from flask import Blueprint, jsonify, request

from services.department_service import department_service

department_app = Blueprint('department_app', __name__)

# Departments API
# university.departments(@id, name, description, department_type)
@department_app.route('/departments/get', methods=['GET'])
def get_departments():
    """ Get all department in JSON format """
    _service = department_service()
    returnStatement = _service.get_departments()
    return jsonify(returnStatement)

@department_app.route('/departments/get/<int:id>', methods=['GET'])
def get_department_by_id(id):
    """ Get a department by ID in JSON format """
    _service = department_service()
    returnStatement = _service.get_department_by_id(id)
    return jsonify(returnStatement)

@department_app.route('/departments/identify', methods=['POST'])
def identify_department():
    """Identify a department by name and degree_type in JSON format"""
    data = request.json
    _service = department_service()
    returnStatement = _service.identify_department(data)
    return jsonify(returnStatement)

@department_app.route('/departments/add', methods=['POST'])
def add_department():
    """ Add a department by data in JSON format """
    data = request.json
    _service = department_service()
    returnStatement = _service.add_department(data)
    
    if returnStatement:
        return jsonify({"message": "Department successfully added!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404

@department_app.route('/departments/delete/<int:id>', methods=['GET'])
def delete_department_by_id(id):
    """ Delete a department by ID in JSON format """
    _service = department_service()
    returnStatement = _service.delete_department_by_id(id)
    
    if returnStatement:
        return jsonify({"message": "Department deleted successfully!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404
    
@department_app.route('/departments/update/<int:id>', methods=['POST'])
def update_department(id):
    """ Update a department record by ID using data in JSON format """
    data = request.json
    _service = department_service()
    updated_department_id = _service.update_department(id, data)
    if updated_department_id:
        return {"message": f"Department record with ID {updated_department_id} updated successfully!"}, 200
    else:
        return {"message": f"Department record with ID {id} not found!"}, 404
