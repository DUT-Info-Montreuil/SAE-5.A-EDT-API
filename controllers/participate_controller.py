from flask import jsonify
from flask import request
from flask import Blueprint

from services.participate_service import participate_service
############################################
##### ? INTEGRER CE CONTROLLER A COURS ?  #####
############################################
# Quand on créer cours ajouter participants?
participate_app = Blueprint('participate_app', __name__)

# Participates API
# university.participates(@id, #course_id, #subgroup_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

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


# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@participate_app.route('/participates/add', methods=['PUT'])
def add_participate():
    """ Add a participate by data in JSON format """
    try:
        data = request.json
        _service = participate_service()
        _service.add_participate(data)
        return jsonify({"message": "Participate successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@participate_app.route('/participates/delete/<int:id>', methods=['DELETE'])
def delete_participate_by_id(id):
    """ Delete a participate by ID in JSON format """
    try:
        _service = participate_service()
        _service.delete_participate_by_id(id)
        return jsonify({"message": "Participate successfully deleted !"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@participate_app.route('/participate/update/<int:id>', methods=['PATCH'])
def update_participate(id):
    """ Update a participate record by ID using data in JSON format """
    try:
        data = request.json
        _service = participate_service()
        _service.update_participate(id, data)
        return jsonify({"message": "Participate successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
