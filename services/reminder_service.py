
from configuration import connect_pg
from services.main_basic_service import *

"""Participates
university.reminders(@id, name, description, #course_id)"""
class reminder_service(Service):
    
    # === region : Reminder ===
    def get_all_reminders(self):
        reminders = Reminder.query.all()
        reminder_list = []

        for reminder in reminders:
            reminder_data = reminder.get_json()
            reminder_list.append(reminder_data)

        return reminder_list
    
    def get_reminder_by_id(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            reminder_data = reminder.get_json()
            return reminder_data
        else:
            return None
    
    def find_reminder(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        reminders = Reminder.query.filter_by(**conditions)

        reminder_list = []

        for reminder in reminders:
            reminder_list.append(reminder.get_json())

        return reminder_list
    
    def delete_reminder(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            db.session.delete(reminder)
            db.session.commit()
            return True
        else:
            return False
    
    def update_reminder(self, reminder_id, new_data):
        reminder = Reminder.query.get(reminder_id)

        if reminder:
            for key, value in new_data.items():
                setattr(reminder, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_reminder(self, reminder_data):
        new_reminder = Reminder(**reminder_data)

        try:
            db.session.add(new_reminder)
            db.session.commit()
            return new_reminder.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Reminder ===