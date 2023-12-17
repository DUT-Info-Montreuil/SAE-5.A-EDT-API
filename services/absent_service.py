from services.main_basic_service import *
from configuration import connect_pg

class absent_service(Service):
    
    # === region : Absent ===
    def get_all_absents(self):
        absents = Absent.query.all()
        absent_list = []

        for absent in absents:
            absent_data = absent.get_json()
            absent_list.append(absent_data)

        return absent_list
    
    def get_absent_by_id(self, absent_id):
        absent = Absent.query.get(absent_id)

        if absent:
            absent_data = absent.get_json()
            return absent_data
        else:
            return None
    
    def find_absent(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        absents = Absent.query.filter_by(**conditions)

        absent_list = []

        for absent in absents:
            absent_list.append(absent.get_json())

        return absent_list
    
    def delete_absent(self, absent_id):
        absent = Absent.query.get(absent_id)

        if absent:
            db.session.delete(absent)
            db.session.commit()
            return True
        else:
            return False
    
    def update_absent(self, absent_id, new_data):
        absent = Absent.query.get(absent_id)

        if absent:
            for key, value in new_data.items():
                setattr(absent, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_absent(self, absent_data):
        new_absent = Absent(**absent_data)

        try:
            db.session.add(new_absent)
            db.session.commit()
            return new_absent.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Absent ===