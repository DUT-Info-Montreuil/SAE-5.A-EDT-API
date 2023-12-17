from services.main_basic_service import *
from configuration import connect_pg

class role_service(Service):
    # === region : Role ===
    def get_all_roles(self):
        roles = Role.query.all()
        role_list = []

        for role in roles:
            role_data = role.get_json()
            role_list.append(role_data)

        return role_list
    
    def get_role_by_id(self, role_id):
        role = Role.query.get(role_id)

        if role:
            role_data = role.get_json()
            return role_data
        else:
            return None
    
    def find_role(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        roles = Role.query.filter_by(**conditions)

        role_list = []

        for role in roles:
            role_list.append(role.get_json())

        return role_list
    
    def delete_role(self, role_id):
        role = Role.query.get(role_id)

        if role:
            db.session.delete(role)
            db.session.commit()
            return True
        else:
            return False
    
    def update_role(self, role_id, new_data):
        role = Role.query.get(role_id)

        if role:
            for key, value in new_data.items():
                setattr(role, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_role(self, role_data):
        new_role = Role(**role_data)

        try:
            db.session.add(new_role)
            db.session.commit()
            return new_role.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Role ===