

from services.specialization_service import specialization_service

specialization_app = Blueprint('specialization_app', __name__)


# Specializations API
# university.specializations(@id, code, name, #department_id)
@specialization_app.route('/specializations/get', methods=['GET'])
def get_specializations():
    """ Get all specializations in JSON format """
    _service = specialization_service()
    returnStatement = _service.get_specializations()
    return jsonify(returnStatement)

@specialization_app.route('/specializations/get/<int:id>', methods=['GET'])
def get_specialization_by_id(id):
    """ Get a specialization by ID in JSON format """
    _service = specialization_service()
    returnStatement = _service.get_specialization_by_id(id)
    return jsonify(returnStatement)

@specialization_app.route('/specializations/identify', methods=['POST'])
def identify_specialization():
    """Identify a specialization by code in JSON format"""
    data = request.json
    _service = specialization_service()
    returnStatement = _service.identify_specialization(data)
    return jsonify(returnStatement)

@specialization_app.route('/specializations/add', methods=['POST'])
def add_specialization():
    """ Add a specialization by data in JSON format """
    data = request.json
    _service = specialization_service()
    returnStatement = _service.add_specialization(data)
    if returnStatement:
        return jsonify({"message": "Specialization successfully added!"}), 200
    else:
        return jsonify({"message": "Specialization not found!"}), 404

@specialization_app.route('/specializations/delete/<int:id>', methods=['GET'])
def delete_specialization_by_id(id):
    """ Delete a specialization by ID in JSON format """
    _service = specialization_service()
    returnStatement = _service.delete_specialization_by_id(id)
    if returnStatement:
        return jsonify({"message": "Specialization deleted successfully!"}), 200
    else:
        return jsonify({"message": "Specialization not found!"}), 404

@specialization_app.route('/specializations/update/<int:id>', methods=['POST'])
def update_specialization(id):
    """ Update a specialization record by ID using data in JSON format """
    data = request.json
    _service = specialization_service()
    updated_specialization_id = _service.update_specialization(id, data)
    if updated_specialization_id:
        return {"message": f"Specialization record with ID {updated_specialization_id} updated successfully!"}, 200
    else:
        return {"message": f"Specialization record with ID {id} not found!"}, 404
