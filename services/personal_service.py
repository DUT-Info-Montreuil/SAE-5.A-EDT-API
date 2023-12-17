from services.main_basic_service import *
from configuration import connect_pg

class personal_service(Service):
    
    # === region : Personal ===
    def get_all_personals(self):
        personals = Personal.query.all()
        personal_list = []

        for personal in personals:
            personal_data = personal.get_json()
            personal_list.append(personal_data)

        return personal_list
    
    def get_personal_by_id(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            personal_data = personal.get_json()
            return personal_data
        else:
            return None
    
    def find_personal(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        personals = Personal.query.filter_by(**conditions)

        personal_list = []

        for personal in personals:
            personal_list.append(personal.get_json())

        return personal_list
    
    def delete_personal(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            db.session.delete(personal)
            db.session.commit()
            return True
        else:
            return False
    
    def update_personal(self, personal_id, new_data):
        personal = Personal.query.get(personal_id)

        if personal:
            for key, value in new_data.items():
                setattr(personal, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_personal(self, personal_data):
        new_personal = Personal(**personal_data)

        try:
            db.session.add(new_personal)
            db.session.commit()
            return new_personal.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Personal ===