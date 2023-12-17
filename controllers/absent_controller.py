from flask import Blueprint, jsonify, request

from services.absent_service import absent_service

absent_app = Blueprint('absent_app', __name__)

# Absents API
# university.absents(@id, description, starttime, duree, absent_type, #personal_id, #rooms_id, #teaching_id)
@absent_app.route('/absents/get', methods=['GET'])
def get_absents():
    """ Get all absents in JSON format """
    _service = absent_service()
    returnStatement = _service.get_absents()
    return jsonify(returnStatement)

@absent_app.route('/absents/get/<int:id>', methods=['GET'])
def get_absent_by_id(id):
    """ Get a absent by ID in JSON format """
    _service = absent_service()
    returnStatement = _service.get_absent_by_id(id)
    return jsonify(returnStatement)

@absent_app.route('/absents/identify', methods=['POST'])
def identify_absent():
    """Identify a absent by description, starttime, duree, absent_type, personal_id, and rooms_id in JSON format"""
    data = request.json
    _service = absent_service()
    returnStatement = _service.identify_absent(data)
    return jsonify(returnStatement)

@absent_app.route('/absents/add', methods=['POST'])
def add_absent():
    """ Add a absent by data in JSON format """
    data = request.json
    _service = absent_service()
    returnStatement = _service.add_absent(data)

    if returnStatement:
        return jsonify({"message": "Absent successfully added!"}), 200
    else:
        return jsonify({"message": "Absent not found!"}), 404

@absent_app.route('/absents/delete/<int:id>', methods=['GET'])
def delete_absent_by_id(id):
    """ Delete a absent by ID in JSON format """
    _service = absent_service()
    returnStatement = _service.delete_absent_by_id(id)
    if returnStatement:
        return jsonify({"message": "Absent deleted successfully!"}), 200
    else:
        return jsonify({"message": "Absent not found!"}), 404
    
@absent_app.route('/absent/update/<int:id>', methods=['POST'])
def update_absent(id):
    """ Update an absent record by ID using data in JSON format """
    data = request.json
    _service = absent_service()
    updated_absent_id = _service.update_absent(id, data)
    if updated_absent_id:
        return {"message": f"Absent record with ID {updated_absent_id} updated successfully!"}, 200
    else:
        return {"message": f"Absent record with ID {id} not found!"}, 404
