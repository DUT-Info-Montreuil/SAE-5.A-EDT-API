from flask import jsonify
from flask import request
from flask import Blueprint

from services.student_service import student_service

student_app = Blueprint('student_app', __name__)

# Students API
# university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
# Faire doc avec swagger, exemple, partager postman et expliquer les fields

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@student_app.route('/students/get', methods=['GET'])
def get_students():
    """ Get all students in JSON format """
    try:
        _service = student_service()
        returnStatement = _service.get_students()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@student_app.route('/students/id/<int:id>', methods=['GET'])
def get_student_by_id(id):
    """ Get a student by id in JSON format """
    try:      
        _service = student_service()
        returnStatement = _service.get_student_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@student_app.route('/students/department/<string:department_id>', methods=['GET'])
def get_student_by_department(department_id):
    """ Get a student by department in JSON format """ 
    try:      
        _service = student_service()
        returnStatement = _service.get_student_by_department(department_id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@student_app.route('/students/groups', methods=['POST'])
def get_student_by_group():
    """ Get a student by department in JSON format """
    try:      
        data = request.json
        _service = student_service()
        returnStatement = _service.get_student_by_group(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@student_app.route('/students/promotion-and-department', methods=['POST'])
def get_student_by_prom():
    """ Get a student by department in JSON format """
    try:      
        data = request.json
        _service = student_service()
        returnStatement = _service.get_student_by_prom(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@student_app.route('/students/subgroups', methods=['POST'])
def get_student_by_subgroup():
    """ Get a student by department in JSON format """
    try:      
        data = request.json
        _service = student_service()
        returnStatement = _service.get_student_by_subgroup(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------


@student_app.route('/students/add', methods=['PUT'])
def add_student():
    """ Add a student by data in JSON format """
    try:
        data = request.json
        _service = student_service()
        _service.get_student_by_subgroup(data)
        return jsonify({"message": "Student successfully added!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


@student_app.route('/students/delete/<int:id>', methods=['DELETE'])
def delete_student_by_id(id):
    """ Delete a student by ID in JSON format """ 
    try:
        _service = student_service()
        _service.delete_student_by_id(id)
        return jsonify({"message": "Student successfully deleted !"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


@student_app.route('/students/update/<int:id>', methods=['PATCH'])
def update_student(id):
    """ Update a student record by id using data in JSON format """
    try:
        data = request.json
        _service = student_service()
        _service.update_student(id, data)
        return jsonify({"message": "Student successfully updated !"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
