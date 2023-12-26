#!/usr/bin/env python
# -*- coding: utf-8 -*-

# === region : Flask and Configuration ===
from flask import Flask
from configuration.config import config


app = Flask(__name__)
# === endregion : Flask ===

# === region : JWT ===
from flask_jwt_extended import JWTManager
from datetime import timedelta
###########################################################

from flask_swagger_ui import get_swaggerui_blueprint

# Register the main controller
app = Flask(__name__)

SWAGGER_URL = '/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
######################################################################
# Config JWT
app.config["JWT_SECRET_KEY"] = "hcohen_aclaude_achetouani_bseydi_mtoure"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15) 
jwt = JWTManager(app)
# === endregion : JWT ===

# === region : SQLAlchemy ===
from flask_sqlalchemy import SQLAlchemy
from services.sql_alchemy_service import *

init_app(app)
# === endregion : SQLAlchemy ===

# === region : blueprint_controller ===
from controllers import *

app.register_blueprint(university_app) # Register the university controller
app.register_blueprint(department_app) # Register the department controller
app.register_blueprint(group_app) # Register the group controller
app.register_blueprint(subgroup_app) # Register the subgroup controller
app.register_blueprint(personal_app) # Register the personal controller
app.register_blueprint(specialization_app) # Register the specialization controller
app.register_blueprint(room_app) # Register the room controller
app.register_blueprint(teaching_app) # Register the teaching controller
app.register_blueprint(role_app) # Register the role controller
app.register_blueprint(course_app) # Register the course controller
app.register_blueprint(student_app) # Register the student controller
app.register_blueprint(responsible_app) # Register the responsible controller
app.register_blueprint(reminder_app) # Register the reminder controller
app.register_blueprint(absent_app) # Register the absent controller
app.register_blueprint(participate_app) # Register the participate controller
app.register_blueprint(auth_app) # Register the autentification controller
app.register_blueprint(user_app) # Register the user controller

# === endregion : blueprint_controller ===

# === region : API ===
from flask_restful import Api
from flask_cors import CORS

cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
# === endregion : blueprint_controller ===

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
  
if __name__ == "__main__":
    # read server parameters
    params = config(section='server')
    # Launch Flask server
    app.run(debug=params['debug'], host=params['host'], port=params['port'])