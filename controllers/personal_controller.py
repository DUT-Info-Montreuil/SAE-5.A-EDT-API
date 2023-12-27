from flask import jsonify
from flask import request
from flask import Blueprint

from services.personal_service import personal_service

personal_app = Blueprint('personal_app', __name__)

# @TO-CHANGE !!!!!!!!!!!!!!!!!!!!!!!!
@personal_app.route('/personals/hours-by-teachers/get/<int:id>', methods=['GET'])
def identify_course(id):
    """Get number of hours of a teacher in JSON format"""
    _service = personal_service()
    returnStatement = _service.identify_course(id)
    return jsonify(returnStatement)

# Personals API
# university.personals(@id, last_name, first_name, mail, phone_number)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@personal_app.route('/personals/get', methods=['GET'])
def get_personals():
    """ Get all personals in JSON format """
    try:
        _service = personal_service()
        returnStatement = _service.get_personals()
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@personal_app.route('/personals/get/<int:id>', methods=['GET'])
def get_personal_by_id(id):
    """ Get a personal by ID in JSON format """
    try:
        _service = personal_service()
        returnStatement = _service.get_personal_by_id(id)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})

@personal_app.route('/personals/identify', methods=['POST'])
def identify_personal():
    """Identify a personal by mail in JSON format"""
    try:
        data = request.json
        _service = personal_service()
        returnStatement = _service.identify_personal(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": str(e)})
    
# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@personal_app.route('/personals/add', methods=['PUT'])
def add_personal():
    """ Add a personal by data in JSON format """
    try:
        data = request.json
        _service = personal_service()
        _service.add_personal(data)
        return jsonify({"message": "Personal successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@personal_app.route('/personals/delete/<int:id>', methods=['DELETE'])
def delete_personal_by_id(id):
    """ Delete a personal by ID in JSON format """
    try:
        _service = personal_service()
        _service.delete_personal_by_id(id)
        return jsonify({"message": "Personal successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@personal_app.route('/personal/update/<int:id>', methods=['PATCH'])
def update_personal(id):
    """ Update a personal record by ID using data in JSON format """
    try:
        data = request.json
        _service = personal_service()
        _service.update_personal(id, data)
        return jsonify({"message": "Personal successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
