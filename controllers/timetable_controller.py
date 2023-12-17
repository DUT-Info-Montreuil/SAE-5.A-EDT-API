from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from services.timetable_service import timetable_service

timetable_app = Blueprint('timetable_app', __name__)

    
@timetable_app.route('/timetable/get/byroom', methods=['POST'])
#@jwt_required()
def get_timetable_by_room():
    """ Get timetable by group"""
    data = request.json
    _service = timetable_service()
    returnStatement = _service.get_timetable_by_room(data)
    if returnStatement == 'Invalid argument':
        return returnStatement
    else:
        return jsonify({'edt' : returnStatement})

@timetable_app.route('/timetable/get/byteacher', methods=['POST'])
#@jwt_required()   
def get_timetable_by_teacher():
    """ Get timetable by teacher_id"""
    data = request.json
    _service = timetable_service()
    returnStatement = _service.get_timetable_by_teacher(data)
    if returnStatement == 'Invalid argument':
        return returnStatement
    else:
        return jsonify({'edt' : returnStatement})
    
@timetable_app.route('/timetable/get/byprom', methods=['POST'])
#@jwt_required()   
def get_timetable_by_prom():
    """ Get timetable by teacher_id"""
    data = request.json
    _service = timetable_service()
    returnStatement = _service.get_timetable_by_prom(data)
    if returnStatement == 'Invalid argument':
        return returnStatement
    else:
        return jsonify({'edt' : returnStatement})
    
@timetable_app.route('/timetable/get/bystudent', methods=['POST'])
#@jwt_required()   
def get_timetable_by_student():
    """ Get timetable by teacher_id"""
    data = request.json
    _service = timetable_service()
    returnStatement = _service.get_timetable_by_student(data)
    if returnStatement == 'Invalid argument':
        return returnStatement
    else:
        return jsonify({'edt' : returnStatement})
    
@timetable_app.route('/timetable/get/bytoken', methods=['POST'])
@jwt_required()
def get_timetable_by_token():
    return jsonify(get_jwt_identity())
    
#via promo

#via userId (pr le dashboard n'affiche que ses groupes)

#via token & userId (pr le dashboard, n'affiche pas les cours de l'autre groupe)
