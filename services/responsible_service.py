from services.main_basic_service import *
from configuration import connect_pg

"""
Participates
university.responsibles(@id, #teaching_id, #personal_id)"""
class responsible_service(Service):
    # === region : Responsible ===
    def get_all_responsibles(self):
        responsibles = Responsible.query.all()
        responsible_list = []

        for responsible in responsibles:
            responsible_data = responsible.get_json()
            responsible_list.append(responsible_data)

        return responsible_list
    
    def get_responsible_by_id(self, responsible_id):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            responsible_data = responsible.get_json()
            return responsible_data
        else:
            return None
    
    def find_responsible(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        responsibles = Responsible.query.filter_by(**conditions)

        responsible_list = []

        for responsible in responsibles:
            responsible_list.append(responsible.get_json())

        return responsible_list
    
    def delete_responsible(self, responsible_id):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            db.session.delete(responsible)
            db.session.commit()
            return True
        else:
            return False
    
    def update_responsible(self, responsible_id, new_data):
        responsible = Responsible.query.get(responsible_id)

        if responsible:
            for key, value in new_data.items():
                setattr(responsible, key, value)

            db.session.commit()
            return True
        else:
            return False
   
    def add_responsible(self, responsible_data):
        new_responsible = Responsible(**responsible_data)

        try:
            db.session.add(new_responsible)
            db.session.commit()
            return new_responsible.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Responsible ===