from flask import jsonify, request, Blueprint


from services.subgroup_service import subgroup_service

subgroup_app = Blueprint('subgroup_app', __name__)

# Subgroups API
# university.subgroups(@id, name, #group_id)
@subgroup_app.route('/subgroups/get', methods=['GET'])
def get_subgroups():
    """ Get all subgroups in JSON format """
    _service = subgroup_service()
    returnStatement = _service.get_subgroups()
    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/get/<int:id>', methods=['GET'])
def get_subgroup_by_id(id):
    """ Get a subgroup by ID in JSON format """
    _service = subgroup_service()
    returnStatement = _service.get_subgroup_by_id(id)
    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/identify', methods=['POST'])
def identify_subgroup():
    """Identify a subgroup by name and group_id in JSON format"""
    data = request.json
    _service = subgroup_service()
    returnStatement = _service.identify_subgroup(data)
    return jsonify(returnStatement)

@subgroup_app.route('/subgroups/add', methods=['POST'])
def add_subgroup():
    """ Add a subgroup by data in JSON format """
    data = request.json
    _service = subgroup_service()
    returnStatement = _service.add_subgroup(data)

    if returnStatement:
        return jsonify({"message": "Subgroup successfully added!"}), 200
    else:
        return jsonify({"message": "Subgroup not found!"}), 404

@subgroup_app.route('/subgroups/delete/<int:id>', methods=['GET'])
def delete_subgroup_by_id(id):
    """ Delete a subgroup by ID in JSON format """
    data = request.json
    _service = subgroup_service()
    returnStatement = _service.delete_subgroup_by_id(id)
    
    if returnStatement:
        return jsonify({"message": "Subgroup deleted successfully!"}), 200
    else:
        return jsonify({"message": "Subgroup not found!"}), 404

@subgroup_app.route('/subgroups/update/<int:id>', methods=['POST'])
def update_subgroup(id):
    """ Update a subgroup record by ID using data in JSON format """
    data = request.json
    _service = subgroup_service()
    updated_subgroup_id = _service.update_subgroup(id, data)
    if updated_subgroup_id:
        return {"message": f"Subgroup record with ID {updated_subgroup_id} updated successfully!"}, 200
    else:
        return {"message": f"Subgroup record with ID {id} not found!"}, 404
