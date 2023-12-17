
from configuration import connect_pg
from services.main_basic_service import *
class participate_service(Service):
    
    # === region : Participate ===
    def get_all_participates(self):
        participates = Participate.query.all()
        participate_list = []

        for participate in participates:
            participate_data = participate.get_json()
            participate_list.append(participate_data)

        return participate_list
    
    def get_participate_by_id(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            participate_data = participate.get_json()
            return participate_data
        else:
            return None
    
    def find_participate(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        participates = Participate.query.filter_by(**conditions)

        participate_list = []

        for participate in participates:
            participate_list.append(participate.get_json())

        return participate_list
    
    def delete_participate(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            db.session.delete(participate)
            db.session.commit()
            return True
        else:
            return False
    
    def update_participate(self, participate_id, new_data):
        participate = Participate.query.get(participate_id)

        if participate:
            for key, value in new_data.items():
                setattr(participate, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_participate(self, participate_data):
        new_participate = Participate(**participate_data)

        try:
            db.session.add(new_participate)
            db.session.commit()
            return new_participate.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Participate ===