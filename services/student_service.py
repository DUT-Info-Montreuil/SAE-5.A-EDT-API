from services.main_basic_service import *

from configuration import connect_pg

"""
Students
university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
"""
class student_service(Service):
    
    # === region : Student ===

    def get_all_students(self):
        students = Student.query.all()
        student_list = []

        for student in students:
            student_data = student.get_json()
            student_list.append(student_data)

        return student_list
    
    def get_student_by_id(self, student_id):
        student = Student.query.get(student_id)

        if student:
            student_data = student.get_json()
            return student_data
        else:
            return None
    
    def find_student(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        students = Student.query.filter_by(**conditions)

        student_list = []

        for student in students:
            student_list.append(student.get_json())

        return student_list
    
    def delete_student(self, student_id):
        student = Student.query.get(student_id)

        if student:
            db.session.delete(student)
            db.session.commit()
            return True
        else:
            return False
    
    def update_student(self, student_id, new_data):
        student = Student.query.get(student_id)

        if student:
            for key, value in new_data.items():
                setattr(student, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_student(self, student_data):
        new_student = Student(**student_data)

        try:
            db.session.add(new_student)
            db.session.commit()
            return new_student.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    
    # === endregion : Student ===

    def get_student_by_prom(self, data):
        department_id = data.get('department_id', '')
        promotion = data.get('promotion', '')

        if promotion == '' or department_id == '':
            return "Null arguments" 

        query = """select * from university.students 
                INNER JOIN university.groups ON university.students.group_id = university.groups.id WHERE 
                university.students.department_id = '""" + department_id + """'
                AND university.groups.promotion = '""" + promotion + """'"""
        
        return self.execute_query_and_get_statement(query)
    
    def execute_query_and_get_statement(self, query):
            conn = self.get_connection()
            rows = connect_pg.get_query(conn, query)
            if rows is None:
                return {}
            returnStatement = []
            for row in rows:
                returnStatement.append(self.get_student_statement(row))
            connect_pg.disconnect(conn)
            return returnStatement

    def get_student_statement(self, row):
        return {
            'student_number': row[0],    # Numero étudiant
            'last_name': row[1],         # Le nom de famille de l'étudiant
            'first_name': row[2],        # Le prénom de l'étudiant
            'mail': row[3],              # L'adresse e-mail de l'étudiant
            'phone_number': row[4],      # Le numéro de téléphone de l'étudiant
            'user_username': row[5],      # Le numéro de téléphone de l'étudiant
            'department_id': row[6],     # L'ID du département auquel l'étudiant est affilié
            'group_id': row[7],          # L'ID du groupe auquel l'étudiant appartient
            'subgroup_id': row[8]        # L'ID du sous-groupe auquel l'étudiant est associé
        }