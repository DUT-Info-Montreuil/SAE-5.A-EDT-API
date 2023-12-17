
from configuration import connect_pg
from services.main_basic_service import *
class department_service(Service):
    
    # === region : Department ===
    def get_all_departments(self):
        departments = Department.query.all()
        department_list = []

        for department in departments:
            department_data = department.get_json()
            department_list.append(department_data)

        return department_list
    
    def get_department_by_id(self, department_id):
        department = Department.query.get(department_id)

        if department:
            department_data = department.get_json()
            return department_data
        else:
            return None
    
    def find_department(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        departments = Department.query.filter_by(**conditions)

        department_list = []

        for department in departments:
            department_list.append(department.get_json())

        return department_list
    
    def delete_department(self, department_id):
        department = Department.query.get(department_id)

        if department:
            db.session.delete(department)
            db.session.commit()
            return True
        else:
            return False
    
    def update_department(self, department_id, new_data):
        department = Department.query.get(department_id)

        if department:
            for key, value in new_data.items():
                setattr(department, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_department(self, department_data):
        new_department = Department(**department_data)

        try:
            db.session.add(new_department)
            db.session.commit()
            return new_department.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Department ===