

from services.group_service import group_service

group_app = Blueprint('group_app', __name__)

# Groups API
# university.groups(@id, promotion, type, #department_id)
@group_app.route('/groups/get', methods=['GET'])
def get_groups():
    """ Get all groups in JSON format """
    _service = group_service()
    returnStatement = _service.get_groups()
    return jsonify(returnStatement)

@group_app.route('/groups/get/<int:id>', methods=['GET'])
def get_group_by_id(id):
    """ Get a group by ID in JSON format """
    _service = group_service()
    returnStatement = _service.get_group_by_id(id)
    return jsonify(returnStatement)

@group_app.route('/groups/identify', methods=['POST'])
def identify_group():
    """Identify a group by promotion and type in JSON format"""
    data = request.json
    _service = group_service()
    returnStatement = _service.identify_group(data)
    return jsonify(returnStatement)

@group_app.route('/groups/add', methods=['POST'])
def add_group():
    """ Add a group by data in JSON format """
    data = request.json
    _service = group_service()
    returnStatement = _service.add_group(data)

    if returnStatement:
        return jsonify({"message": "Group successfully added!"}), 200
    else:
        return jsonify({"message": "Group not found!"}), 404

@group_app.route('/groups/delete/<int:id>', methods=['GET'])
def delete_group_by_id(id):
    """ Delete a group by ID in JSON format """
    _service = group_service()
    returnStatement = _service.delete_group_by_id(id)
    if returnStatement:
        return jsonify({"message": "Department deleted successfully!"}), 200
    else:
        return jsonify({"message": "Department not found!"}), 404
    
@group_app.route('/groups/update/<int:id>', methods=['POST'])
def update_group(id):
    """ Update a group record by ID using data in JSON format """
    data = request.json
    _service = group_service()
    updated_group_id = _service.update_group(id, data)
    if updated_group_id:
        return {"message": f"Group record with ID {updated_group_id} updated successfully!"}, 200
    else:
        return {"message": f"Group record with ID {id} not found!"}, 404
