from services.main_service import Service

import connect_pg

class student_service(Service):
    
    # Students API
    # university.students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)

    # Recuperer departement

    # ----------------------------------------------------------
    # Recuperer data
    # ----------------------------------------------------------

    def get_students(self):
        """ Get all students in JSON format """
        
        query = "SELECT * FROM university.students"
        return self.execute_query_and_get_statement(query)
    
    def get_student_by_student_number(self, student_number):
        """ Get a student by student_number in JSON format """

        query = "SELECT * FROM university.students WHERE student_number = '" + student_number + "'"
        return self.execute_query_and_get_statement(query)
    
    def get_student_by_department(self, department_id):

        query = "SELECT * FROM university.students WHERE department_id = '" + department_id + "'"
        return self.execute_query_and_get_statement(query)
    
    def get_student_by_group(self, data):
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')

        if group_id == '' or department_id == '':
            return "Null arguments" 

        query = "SELECT * FROM university.students WHERE department_id = '" + department_id + "' AND group_id = '" + group_id + "'"
        return self.execute_query_and_get_statement(query)
    
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
    
    # TO-DO recuperer un apprenti/ un parcours A / ...
    # def get_student_by_group_type(self, data):
    #     department_id = data.get('department_id', '')
    #     promotion = data.get('promotion', '')

    #     if promotion == '' or department_id == '':
    #         return "Null arguments" 

    #     query = """select * from university.students 
    #             INNER JOIN university.groups ON university.students.group_id = university.groups.id WHERE 
    #             university.students.department_id = '""" + department_id + """'
    #             AND university.groups.promotion = '""" + promotion + """'"""
        
    #     return self.execute_query_and_get_statement(query)
    
    def get_student_by_subgroup(self,data):
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')
        subgroup_id = data.get('subgroup_id', '')

        if group_id == '' or department_id == '' or subgroup_id == '':
            return "Null arguments" 

        query = "SELECT * FROM university.students WHERE department_id = '" + department_id + "' AND group_id = '" + group_id + "' AND subgroup_id = '" + subgroup_id  + "'"
        return self.execute_query_and_get_statement(query)
    
    
    
    # ----------------------------------------------------------
    # Add / Delete / Update
    # ----------------------------------------------------------

    def add_student(self, data):
        """ Add a student by data in JSON format """

        student_number = data.get('student_number', '') # MODIFIER !!!!!!!!!!!!
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
        username = data.get('username')
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')
        subgroup_id = data.get('subgroup_id', '')

        query = "INSERT INTO university.students (student_number, last_name, first_name, mail, phone_number, user_username, department_id, group_id, subgroup_id) VALUES ('" + student_number+ "', '" + last_name+ "', '" + first_name+ "', '" + mail + "', '" + phone_number+ "', '" + username+ "', " + department_id+ ", " + group_id+ ", " + subgroup_id+ ")"

        conn = self.get_connection()
        new_student_number = connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)
    
        return new_student_number

    
    def delete_student_by_id(self, student_number):
        """ Delete a student by ID in JSON format """
        
        query = "DELETE FROM university.students WHERE student_number = '" + str(student_number) + "'" 

        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)
        return row
    
    def update_student(self, student_number, data):
        """ Update a student record by student_number using data in JSON format """
        # data = request.json

        # Check if the student record with the given student_number exists
        existing_student = self.get_student_by_student_number(student_number)
        if not existing_student:
            return existing_student

        last_name = data.get('last_name', existing_student['last_name'])
        first_name = data.get('first_name', existing_student['first_name'])
        mail = data.get('mail', existing_student['mail'])
        phone_number = data.get('phone_number', existing_student['phone_number'])
        department_id = data.get('department_id', existing_student['department_id'])
        group_id = data.get('group_id', existing_student['group_id'])
        subgroup_id = data.get('subgroup_id', existing_student['subgroup_id'])

        query = """UPDATE university.students
                SET last_name = '" + last_name+ "',
                    first_name = '" + first_name+ "',
                    mail = '" + mail+ "',
                    phone_number = '" + phone_number+ "',
                    department_id = " + department_id+ ",
                    group_id = " + group_id+ ",
                    subgroup_id = " + subgroup_id+ "
                WHERE student_number = '" + student_number+ "'
                RETURNING student_number """ % {
                    'student_number': student_number,
                    'last_name': last_name,
                    'first_name': first_name,
                    'mail': mail,
                    'phone_number': phone_number,
                    'department_id': department_id,
                    'group_id': group_id,
                    'subgroup_id': subgroup_id
                }

        conn = self.get_connection()
        updated_student_number = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_student_number

    # ----------------------------------------------------------
    # Utilitaires
    # ----------------------------------------------------------

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