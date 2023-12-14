from services.main_service import Service

from configuration import connect_pg

class student_service(Service):
    
    # Students API
    # students(@id, last_name, first_name, mail, phone_number, #department_id, #group_id, #subgroup_id)
    def get_students(self):
        """ Get all students in JSON format """
        
        query = "SELECT * FROM students"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_student_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_student_by_student_number(self, student_number):
        """ Get a student by student_number in JSON format """

        query = "SELECT * FROM students WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_student_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_student(self, data):
        """Identify a student by last_name, first_name, mail, phone_number, department_id, group_id and subgroup_id in JSON format"""
        # data = request.json
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')
        subgroup_id = data.get('subgroup_id', '')
    
        query = "SELECT * FROM students WHERE last_name = '%(last_name)s' AND first_name = '%(first_name)s' AND mail = '%(mail)s' AND phone_number = '%(phone_number)s' AND department_id = %(department_id)s AND group_id = %(group_id)s AND subgroup_id = %(subgroup_id)s" % {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number, 'department_id': department_id, 'group_id': group_id, 'subgroup_id': subgroup_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_student_statement(row))
    
        return returnStatement
    
    def add_student(self, data):
        """ Add a student by data in JSON format """
        # data = request.json
    
        student_number = data.get('student_number', '')
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')
        subgroup_id = data.get('subgroup_id', '')
    
        query = "INSERT INTO students (student_number, last_name, first_name, mail, phone_number, department_id, group_id, subgroup_id) VALUES ('%(student_number)s', '%(last_name)s', '%(first_name)s', '%(mail)s', '%(phone_number)s', %(department_id)s, %(group_id)s, %(subgroup_id)s) RETURNING id" % {'student_number': student_number, 'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number, 'department_id': department_id, 'group_id': group_id, 'subgroup_id': subgroup_id}
        conn = self.get_connection()
        new_student_number = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_student_number
    
    def delete_student_by_id(self, student_number):
        """ Delete a student by ID in JSON format """
        
        query = "DELETE FROM students WHERE student_number = '%(student_number)s' RETURNING student_number" %  {'student_number': student_number}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
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

        query = """UPDATE students
                SET last_name = '%(last_name)s',
                    first_name = '%(first_name)s',
                    mail = '%(mail)s',
                    phone_number = '%(phone_number)s',
                    department_id = %(department_id)s,
                    group_id = %(group_id)s,
                    subgroup_id = %(subgroup_id)s
                WHERE student_number = '%(student_number)s'
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

    
    def get_student_statement(self, row):
        return {
            'student_number': row[0],    # Numero étudiant
            'last_name': row[1],         # Le nom de famille de l'étudiant
            'first_name': row[2],        # Le prénom de l'étudiant
            'mail': row[3],              # L'adresse e-mail de l'étudiant
            'phone_number': row[4],      # Le numéro de téléphone de l'étudiant
            'department_id': row[5],     # L'ID du département auquel l'étudiant est affilié
            'group_id': row[6],          # L'ID du groupe auquel l'étudiant appartient
            'subgroup_id': row[7]        # L'ID du sous-groupe auquel l'étudiant est associé
        }