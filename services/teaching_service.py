from services.main_basic_service import *

from configuration import connect_pg

"""
Teachings
university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)"""
class teaching_service(Service):
    
    # === region : Teaching ===
    def get_all_teachings(self):
        teachings = Teaching.query.all()
        teaching_list = []

        for teaching in teachings:
            teaching_data = teaching.get_json()
            teaching_list.append(teaching_data)

        return teaching_list
    
    def get_teaching_by_id(self, teaching_id):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            teaching_data = teaching.get_json()
            return teaching_data
        else:
            return None
    
    def find_teaching(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        teachings = Teaching.query.filter_by(**conditions)

        teaching_list = []

        for teaching in teachings:
            teaching_list.append(teaching.get_json())

        return teaching_list
    
    def delete_teaching(self, teaching_id):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            db.session.delete(teaching)
            db.session.commit()
            return True
        else:
            return False
    
    def update_teaching(self, teaching_id, new_data):
        teaching = Teaching.query.get(teaching_id)

        if teaching:
            for key, value in new_data.items():
                setattr(teaching, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_teaching(self, teaching_data):
        new_teaching = Teaching(**teaching_data)

        try:
            db.session.add(new_teaching)
            db.session.commit()
            return new_teaching.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Teaching ===