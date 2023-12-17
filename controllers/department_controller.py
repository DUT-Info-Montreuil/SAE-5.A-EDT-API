from flask import jsonify
from flask import request
from flask import Blueprint

from services.department_service import department_service

department_app = Blueprint('department_app', __name__)

# Departments API
# university.departments(@id, name, description, department_type)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

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

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@department_app.route('/departments/add', methods=['PUT'])
def add_department():
    """ Add a department by data in JSON format """
    try:
        data = request.json
        _service = department_service()
        _service.add_department(data)
        return jsonify({"message": "Department successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@department_app.route('/departments/delete/<int:id>', methods=['DELETE'])
def delete_department_by_id(id):
    """ Delete a department by ID in JSON format """ 
    try:
        _service = department_service()
        _service.delete_department_by_id(id)
        return jsonify({"message": "Department successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@department_app.route('/departments/update/<int:id>', methods=['PATCH'])
def update_department(id):
    """ Update a department record by ID using data in JSON format """
    try:
        data = request.json
        _service = department_service()
        _service.update_department(id, data)
        return jsonify({"message": "Department successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
