from services.main_basic_service import *

from configuration import connect_pg
"""
Specializations
university.specializations(@id, code, name, #department_id)"""
class specialization_service(Service):
    
    # === region : Specialization ===
    def get_all_specializations(self):
        specializations = Specialization.query.all()
        specialization_list = []

        for specialization in specializations:
            specialization_data = specialization.get_json()
            specialization_list.append(specialization_data)

        return specialization_list
    
    def get_specialization_by_id(self, specialization_id):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            specialization_data = specialization.get_json()
            return specialization_data
        else:
            return None
    
    def find_specialization(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        specializations = Specialization.query.filter_by(**conditions)

        specialization_list = []

        for specialization in specializations:
            specialization_list.append(specialization.get_json())

        return specialization_list
    
    def delete_specialization(self, specialization_id):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            db.session.delete(specialization)
            db.session.commit()
            return True
        else:
            return False
    
    def update_specialization(self, specialization_id, new_data):
        specialization = Specialization.query.get(specialization_id)

        if specialization:
            for key, value in new_data.items():
                setattr(specialization, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_specialization(self, specialization_data):
        new_specialization = Specialization(**specialization_data)

        try:
            db.session.add(new_specialization)
            db.session.commit()
            return new_specialization.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Specialization ===
    
    