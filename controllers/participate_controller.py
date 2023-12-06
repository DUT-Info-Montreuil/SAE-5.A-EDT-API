from flask import jsonify, request, Blueprint


from services.participate_service import participate_service

participate_app = Blueprint('participate_app', __name__)

# Participates API
# university.participates(@id, #course_id, #subgroup_id)
@participate_app.route('/participates/get', methods=['GET'])
def get_participates():
    """ Get all participates in JSON format """
    _service = participate_service()
    returnStatement = _service.get_participates()
    return jsonify(returnStatement)

@participate_app.route('/participates/get/<int:id>', methods=['GET'])
def get_participate_by_id(id):
    """ Get a participate by ID in JSON format """
    _service = participate_service()
    returnStatement = _service.get_participate_by_id(id)
    return jsonify(returnStatement)

@participate_app.route('/participates/identify', methods=['POST'])
def identify_participate():
    """Identify a participate by course_id and subgroup_id in JSON format"""
    data = request.json
    _service = participate_service()
    returnStatement = _service.identify_participate(data)
    return jsonify(returnStatement)

@participate_app.route('/participates/add', methods=['POST'])
def add_participate():
    """ Add a participate by data in JSON format """
    data = request.json
    _service = participate_service()
    returnStatement = _service.add_participate(data)

    if returnStatement:
        return jsonify({"message": "Course successfully added!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404

@participate_app.route('/participates/delete/<int:id>', methods=['GET'])
def delete_participate_by_id(id):
    """ Delete a participate by ID in JSON format """
    _service = participate_service()
    returnStatement = _service.delete_participate_by_id(id)
    if returnStatement:
        return jsonify({"message": "Course deleted successfully!"}), 200
    else:
        return jsonify({"message": "Course not found!"}), 404
    
@participate_app.route('/participate/update/<int:id>', methods=['POST'])
def update_participate(id):
    """ Update a participate record by ID using data in JSON format """
    data = request.json
    _service = participate_service()
    updated_participate_id = _service.update_participate(id, data)
    if updated_participate_id:
        return {"message": f"Participate record with ID {updated_participate_id} updated successfully!"}, 200
    else:
        return {"message": f"Participate record with ID {id} not found!"}, 404
