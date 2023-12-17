from flask import jsonify
from flask import request
from flask import Blueprint

from services.reminder_service import reminder_service

reminder_app = Blueprint('reminder_app', __name__)


# Reminders API
# university.reminders(@id, #course_id, #subgroup_id)

# ----------------------------------------------------------
# Recuperer data
# ----------------------------------------------------------

@reminder_app.route('/reminders/get', methods=['GET'])
def get_reminders():
    """ Get all reminders in JSON format """
    _service = reminder_service()
    returnStatement = _service.get_reminders()
    return jsonify(returnStatement)

@reminder_app.route('/reminders/get/<int:id>', methods=['GET'])
def get_reminder_by_id(id):
    """ Get a reminder by ID in JSON format """
    _service = reminder_service()
    returnStatement = _service.get_reminder_by_id(id)
    return jsonify(returnStatement)

@reminder_app.route('/reminders/identify', methods=['POST'])
def identify_reminder():
    """Identify a reminder by course_id and subgroup_id in JSON format"""
    data = request.json
    _service = reminder_service()
    returnStatement = _service.identify_reminder(data)
    return jsonify(returnStatement)

# ----------------------------------------------------------
# Add / Delete / Update
# ----------------------------------------------------------

@reminder_app.route('/reminders/add', methods=['PUT'])
def add_reminder():
    """ Add a reminder by data in JSON format """
    try:
        data = request.json
        _service = reminder_service()
        _service.add_reminder(data)
        return jsonify({"message": "Reminder successfully added !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404

@reminder_app.route('/reminders/delete/<int:id>', methods=['DELETE'])
def delete_reminder_by_id(id):
    """ Delete a reminder by ID in JSON format """
    try:
        _service = reminder_service()
        _service.delete_reminder_by_id(id)
        return jsonify({"message": "Reminder successfully deleted !"}), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
    
@reminder_app.route('/reminders/update/<int:id>', methods=['PATCH'])
def update_reminder(id):
    """ Update a reminder record by ID using data in JSON format """
    try:
        data = request.json
        _service = reminder_service()
        _service.update_reminder(id, data)
        return jsonify({"message": "Reminder successfully updated!"}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 404
