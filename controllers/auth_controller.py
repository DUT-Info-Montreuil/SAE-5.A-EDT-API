from flask import jsonify, request, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token

from services.auth_service import auth_service

auth_app = Blueprint('auth_app', __name__)

# verif username/mdp
@auth_app.route('/auth/login', methods=['POST'])
def login():
    """" Authentification method by login, and password """
    data = request.json
    _service = auth_service()
    returnStatement = _service.login(data)
    if returnStatement == "Bad username or password" : 
        return jsonify({"msg": returnStatement}), 401
    elif returnStatement == "Username or password not filled":
        return jsonify({"msg": returnStatement})
    else:
        access_token = create_access_token(identity=returnStatement)
        return jsonify({'token':access_token})

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@auth_app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


# deconnexion
#@auth_app.route('/auth/logout')




## Service 

#hash password / unshash


# deconnexion

# Verif token

# Create token

# Delete token