#!/usr/bin/env python
# -*- coding: utf-8 -*-

# === region : Flask and Configuration ===
from flask import Flask
from configuration.config import config


app = Flask(__name__)
# === endregion : Flask ===

# === region : JWT ===
from flask_jwt_extended import JWTManager, jwt_required
from datetime import timedelta

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

def apply_jwt_middleware(blueprint):
    @blueprint.before_request
    @jwt_required()
    def before_request():
        pass

apply_jwt_middleware(department_app)
apply_jwt_middleware(group_app)
apply_jwt_middleware(subgroup_app)
apply_jwt_middleware(personal_app)
apply_jwt_middleware(specialization_app)
apply_jwt_middleware(room_app)
apply_jwt_middleware(teaching_app) 
apply_jwt_middleware(role_app)
apply_jwt_middleware(course_app) 
apply_jwt_middleware(student_app) 
apply_jwt_middleware(responsible_app) 
apply_jwt_middleware(reminder_app)
apply_jwt_middleware(absent_app)
apply_jwt_middleware(participate_app) 
apply_jwt_middleware(user_app)
apply_jwt_middleware(rooms_courses_app) 
apply_jwt_middleware(personals_courses_app) 

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
app.register_blueprint(rooms_courses_app) # Register the rooms_courses controller
app.register_blueprint(personals_courses_app) # Register the personals_courses controller

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