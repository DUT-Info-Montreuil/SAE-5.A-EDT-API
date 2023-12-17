from flask import Blueprint, jsonify, request
from services.user_service import UserService
user_app = Blueprint('user_app', __name__)
userService = UserService()

@user_app.route('/users', methods=['GET'])
def get_users():
    users = userService.get_all_users()
    return jsonify({'users': users})

@user_app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = userService.get_user_by_id(user_id)

    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404


@user_app.route('/users/find', methods=['POST'])
def find_user():
    data = request.get_json()
    user = userService.find_user(**data)

    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 404
    
@user_app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    success = userService.update_user(user_id, data)

    if success:
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404
    
@user_app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    success = userService.delete_user(user_id)

    if success:
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404

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
