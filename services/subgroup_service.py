
from services.main_basic_service import *

from configuration import connect_pg
"""
Subgroups
university.subgroups(@id, name, #group_id)"""
class subgroup_service(Service):
    
    # === region : Subgroup ===
    def get_all_subgroups(self):
        subgroups = Subgroup.query.all()
        subgroup_list = []

        for subgroup in subgroups:
            subgroup_data = subgroup.get_json()
            subgroup_list.append(subgroup_data)

        return subgroup_list
    
    def get_subgroup_by_id(self, subgroup_id):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            subgroup_data = subgroup.get_json()
            return subgroup_data
        else:
            return None
    
    def find_subgroup(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        subgroups = Subgroup.query.filter_by(**conditions)

        subgroup_list = []

        for subgroup in subgroups:
            subgroup_list.append(subgroup.get_json())

        return subgroup_list
    
    def delete_subgroup(self, subgroup_id):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            db.session.delete(subgroup)
            db.session.commit()
            return True
        else:
            return False
    
    def update_subgroup(self, subgroup_id, new_data):
        subgroup = Subgroup.query.get(subgroup_id)

        if subgroup:
            for key, value in new_data.items():
                setattr(subgroup, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_subgroup(self, subgroup_data):
        new_subgroup = Subgroup(**subgroup_data)

        try:
            db.session.add(new_subgroup)
            db.session.commit()
            return new_subgroup.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Subgroup ===