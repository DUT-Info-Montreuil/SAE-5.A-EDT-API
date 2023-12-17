from flask import jsonify
from flask import request
from flask import Blueprint

from services.user_service import user_service

user_app = Blueprint('user_app', __name__)

#should it be protected?, do we need an endpoint ? 
@user_app.route('/user/add', methods=['PUT'])
def add_user():
    """ Get all students in JSON format """
    try:
        data = request.json
        _service = user_service()
        returnStatement = _service.add_user(data)
        return jsonify(returnStatement)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
