from flask import jsonify
from flask import request
from flask import Blueprint

from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies

from services.auth_service import auth_service

from datetime import timedelta

auth_app = Blueprint('auth_app', __name__)

# verif username/mdp
@auth_app.route('/auth/login', methods=['POST'])
def login():
    """ Authentication method by login and password """
    try:
        data = request.json
        _service = auth_service()
        returnStatement = _service.login(data)

        if returnStatement == "Bad username or password":
            return jsonify({"msg": returnStatement}), 401
        elif returnStatement == "Username or password not filled":
            return jsonify({"msg": returnStatement})
        else:
            access_token = create_access_token(identity=returnStatement)
            response = jsonify({'token': access_token})
            set_access_cookies(response, access_token)
            return jsonify({'token': access_token})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@auth_app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    try:
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


## Service 

#hash password / unshash

#refresh token

# deconnexion
@auth_app.route('/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    try:
        # Accéder au jeton JWT brut depuis la requête
        current_user = get_jwt_identity()
        print(f"logout : {current_user}")
        
        # Créer un nouveau jeton avec un temps d'expiration court pour invalider le jeton actuel
        access_token = create_access_token(identity=None, expires_delta=timedelta(secondes=0))
        response = jsonify({'token': access_token})
        set_access_cookies(response, access_token)
        unset_jwt_cookies(response)
        return jsonify({'msg': 'Déconnexion réussie', 'new_token': access_token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Verif token

# Create token

# Delete token
    #si nouveaux token delete ancien ? ou empecher creation token?