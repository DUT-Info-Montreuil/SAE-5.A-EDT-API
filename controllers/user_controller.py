from flask import Blueprint, jsonify, request
from services.user_service import UserService
user_app = Blueprint('user_app', __name__)
userService = UserService()

@user_app.route('/users/get', methods=['GET'])
def get_users():
    try:
        users = userService.get_all_users()
        return jsonify({'users': users})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@user_app.route('/users/get/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        user = userService.get_user_by_id(user_id)
        return jsonify({'user': user})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404


@user_app.route('/users/find', methods=['POST'])
def find_user():
    try:
        data = request.get_json()
        userService.find_user(**data)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@user_app.route('/users/update/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    try:
        data = request.get_json()
        userService.update_user(user_id, data)
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@user_app.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        userService.delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

   
#should it be protected?, do we need an endpoint ? 
@user_app.route('/user/add', methods=['PUT'])
def add_user():
    """ Get all students in JSON format """
    try:
        data = request.json
        userService.add_user(data)     
        return jsonify({'message': 'User added successfully'})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
