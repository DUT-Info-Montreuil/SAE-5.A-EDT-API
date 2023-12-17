
from configuration import connect_pg
from services.main_basic_service import *
class group_service(Service):
    
    # === region : Group ===
    def get_all_groups(self):
        groups = Group.query.all()
        group_list = []

        for group in groups:
            group_data = group.get_json()
            group_list.append(group_data)

        return group_list
    
    def get_group_by_id(self, group_id):
        group = Group.query.get(group_id)

        if group:
            group_data = group.get_json()
            return group_data
        else:
            return None
    
    def find_group(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        groups = Group.query.filter_by(**conditions)

        group_list = []

        for group in groups:
            group_list.append(group.get_json())

        return group_list
    
    def delete_group(self, group_id):
        group = Group.query.get(group_id)

        if group:
            db.session.delete(group)
            db.session.commit()
            return True
        else:
            return False
    
    def update_group(self, group_id, new_data):
        group = Group.query.get(group_id)

        if group:
            for key, value in new_data.items():
                setattr(group, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_group(self, group_data):
        new_group = Group(**group_data)

        try:
            db.session.add(new_group)
            db.session.commit()
            return new_group.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Group ===