from flask import Blueprint, jsonify, request
from services.reminder_service import reminder_service

reminder_app = Blueprint('reminder_app', __name__)
reminderService = reminder_service()

@reminder_app.route('/reminders/get', methods=['GET'])
def get_reminders():
    reminders = reminderService.get_all_reminders()
    return jsonify({'reminders': reminders})

@reminder_app.route('/reminders/get/<int:reminder_id>', methods=['GET'])
def get_reminder_by_id(reminder_id):
    reminder = reminderService.get_reminder_by_id(reminder_id)

    if reminder:
        return jsonify({'reminder': reminder})
    else:
        return jsonify({'message': 'Reminder not found'}), 404

@reminder_app.route('/reminders/identify', methods=['POST'])
def find_reminder():
    data = request.get_json()
    reminder = reminderService.find_reminder(**data)

    if reminder:
        return jsonify({'reminder': reminder})
    else:
        return jsonify({'message': 'Reminder not found'}), 404
    
@reminder_app.route('/reminders/update/<int:reminder_id>', methods=['PATCH'])
def update_reminder(reminder_id):
    data = request.get_json()
    success = reminderService.update_reminder(reminder_id, data)

    if success:
        return jsonify({'message': 'Reminder updated successfully'})
    else:
        return jsonify({'message': 'Reminder not found'}), 404
    
@reminder_app.route('/reminders/delete/<int:reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    success = reminderService.delete_reminder(reminder_id)

    if success:
        return jsonify({'message': 'Reminder deleted successfully'})
    else:
        return jsonify({'message': 'Reminder not found'}), 404

@reminder_app.route('/reminders/add', methods=['PUT'])
def add_reminder():
    
    data = request.json
    success = reminderService.add_reminder(data)
    
    if success:
        return jsonify(success)
    else:
        return jsonify({'message': 'Reminder not add'}), 404