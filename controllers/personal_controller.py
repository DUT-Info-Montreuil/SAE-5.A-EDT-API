from flask import jsonify, request, Blueprint


from services.personal_service import personal_service

personal_app = Blueprint('personal_app', __name__)

# Personals API
# university.personals(@id, last_name, first_name, mail, phone_number)
@personal_app.route('/personals/get', methods=['GET'])
def get_personals():
    """ Get all personals in JSON format """
    _service = personal_service()
    returnStatement = _service.get_personals()
    return jsonify(returnStatement)

@personal_app.route('/personals/get/<int:id>', methods=['GET'])
def get_personal_by_id(id):
    """ Get a personal by ID in JSON format """
    _service = personal_service()
    returnStatement = _service.get_personal_by_id(id)
    return jsonify(returnStatement)

@personal_app.route('/personals/identify', methods=['POST'])
def identify_personal():
    """Identify a personal by mail in JSON format"""
    data = request.json
    _service = personal_service()
    returnStatement = _service.identify_personal(data)
    return jsonify(returnStatement)

@personal_app.route('/personals/add', methods=['POST'])
def add_personal():
    """ Add a personal by data in JSON format """
    data = request.json
    _service = personal_service()
    returnStatement = _service.add_personal(data)
    if returnStatement:
        return jsonify({"message": "Personal successfully added!"}), 200
    else:
        return jsonify({"message": "Personal not found!"}), 404

@personal_app.route('/personals/delete/<int:id>', methods=['GET'])
def delete_personal_by_id(id):
    """ Delete a personal by ID in JSON format """
    _service = personal_service()
    returnStatement = _service.delete_personal_by_id(id)
    if returnStatement:
        return jsonify({"message": "Personal deleted successfully!"}), 200
    else:
        return jsonify({"message": "Personal not found!"}), 404

@personal_app.route('/personal/update/<int:id>', methods=['POST'])
def update_personal(id):
    """ Update a personal record by ID using data in JSON format """
    data = request.json
    _service = personal_service()
    updated_personal_id = _service.update_personal(id, data)
    if updated_personal_id:
        return {"message": f"Personal record with ID {updated_personal_id} updated successfully!"}, 200
    else:
        return {"message": f"Personal record with ID {id} not found!"}, 404
