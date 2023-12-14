from flask import jsonify
from flask import request
from flask import Blueprint

from services.student_service import student_service

student_app = Blueprint('student_app', __name__)

# Students API
# university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
# Faire doc avec swagger, exemple, partager postman et expliquer les fields

@student_app.route('/students/get', methods=['GET'])
def get_students():
    """ Get all students in JSON format """
    _service = student_service()
    returnStatement = _service.get_students()
    return jsonify(returnStatement)

@student_app.route('/students/id/<string:student_number>', methods=['GET'])
def get_student_by_student_number(student_number):
    """ Get a student by student_number in JSON format """
    
    _service = student_service()
    returnStatement = _service.get_student_by_student_number(student_number)
    return jsonify(returnStatement)

@student_app.route('/students/department/<string:department_id>', methods=['GET'])
def get_student_by_department(department_id):
    """ Get a student by department in JSON format """
    
    _service = student_service()
    returnStatement = _service.get_student_by_department(department_id)
    return jsonify(returnStatement)

@student_app.route('/students/groups', methods=['POST'])
def get_student_by_group():
    """ Get a student by department in JSON format """
    data = request.json
    _service = student_service()
    returnStatement = _service.get_student_by_group(data)
    return jsonify(returnStatement)

@student_app.route('/students/subgroups', methods=['POST'])
def get_student_by_subgroup():
    """ Get a student by department in JSON format """
    data = request.json
    _service = student_service()
    returnStatement = _service.get_student_by_subgroup(data)
    return jsonify(returnStatement)

#Before creating a student insert a user
@student_app.route('/students/add', methods=['PUT'])
def add_student():
    """ Add a student by data in JSON format """

    data = request.json
    _service = student_service()
    returnStatement = _service.add_student(data)

    ## Changer ça!
    if returnStatement:
        return jsonify({"message": "Student successfully added!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

@student_app.route('/students/delete/<string:student_number>', methods=['GET'])
def delete_student_by_id(student_number):
    """ Delete a student by ID in JSON format """
    _service = student_service()
    returnStatement = _service.delete_student_by_id(student_number)
    #conditionner return statement
    if returnStatement:
        return jsonify({"message": "Student deleted successfully!"}), 200
    else:
        return jsonify({"message": "Student not found!"}), 404

@student_app.route('/students/update/<string:student_number>', methods=['POST'])
def update_student(student_number):
    """ Update a student record by student_number using data in JSON format """
    data = request.json
    _service = student_service()
    updated_student_number = _service.update_student(student_number, data)
    if updated_student_number:
        return {"message": f"Student record with student number {updated_student_number} updated successfully!"}, 200
    else:
        return {"message": f"Student record with student number {student_number} not found!"}, 404
