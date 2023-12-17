from flask import jsonify
from flask import request
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from services.timetable_service import timetable_service

timetable_app = Blueprint('timetable_app', __name__)

    
@timetable_app.route('/timetable/get/byroom', methods=['POST'])
#@jwt_required()
def get_timetable_by_room():
    """ Get timetable by group"""
    try:
        data = request.json
        _service = timetable_service()
        return _service.get_timetable_by_room(data)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@timetable_app.route('/timetable/get/byteacher', methods=['POST'])
#@jwt_required()   
def get_timetable_by_teacher():
    """ Get timetable by teacher_id"""
    try:
        data = request.json
        _service = timetable_service()
        return _service.get_timetable_by_teacher(data)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@timetable_app.route('/timetable/get/byprom', methods=['POST'])
#@jwt_required()   
def get_timetable_by_prom():
    """ Get timetable by teacher_id"""
    try:
        data = request.json
        _service = timetable_service()
        return _service.get_timetable_by_prom(data)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@timetable_app.route('/timetable/get/bystudent', methods=['POST'])
#@jwt_required()   
def get_timetable_by_student():
    """ Get timetable by teacher_id"""
    try:
        data = request.json
        _service = timetable_service()
        return _service.get_timetable_by_student(data)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
    
@timetable_app.route('/timetable/get/bytoken', methods=['POST'])
@jwt_required()
def get_timetable_by_token():
    return jsonify(get_jwt_identity())
    
#via promo

#via userId (pr le dashboard n'affiche que ses groupes)

#via token & userId (pr le dashboard, n'affiche pas les cours de l'autre groupe)
