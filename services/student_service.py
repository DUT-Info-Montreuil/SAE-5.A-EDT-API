from services.main_service import Service

from configuration import connect_pg

from services.user_service import UserService

class student_service(Service):
    
    # Students API
    # university.students(@id, last_name, first_name, #department_id, #group_id, #subgroup_id)

    # Recuperer departement

    # ----------------------------------------------------------
    # Recuperer data
    # ----------------------------------------------------------

    def get_students(self):
        """ Get all students in JSON format """
        
        query = "SELECT * FROM university.students"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_student_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    

    def get_student_by_id(self, id):
        """ Get a student by id in JSON format """

        query = "SELECT * FROM university.students WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_student_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    

    def get_student_by_department(self, id):

        query = "SELECT * FROM university.students WHERE department_id = '" + id + "'"
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
        _userService = UserService()
                
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        department_id = data.get('department_id', '')
        group_id = data.get('group_id', '')
        subgroup_id = data.get('subgroup_id', '')

        userData = {
            "username": data["first_name"][0].lower() + data["last_name"].lower(),
            "password": data["password"]
        }

        new_user_id = _userService.add_user(userData)

        query = "INSERT INTO university.students (last_name, first_name, user_id, department_id, group_id, subgroup_id) VALUES ('%(last_name)s', '%(first_name)s', %(new_user_id)s, %(department_id)s, %(group_id)s, %(subgroup_id)s ) RETURNING id" % {'last_name': last_name, 'first_name': first_name, 'new_user_id': new_user_id, 'department_id': department_id, 'group_id': group_id, 'subgroup_id': subgroup_id}                                                                                                                                                               
        print(query)
        conn = self.get_connection()
        new_id = connect_pg.execute_commands(conn, (query,))
        #connect_pg.disconnect(conn)
    
        return new_id

    
    def delete_student_by_id(self, id):
        """ Delete a student by ID in JSON format """
        _userService = UserService()
        student = self.get_student_by_id(id)
           
        query = "DELETE FROM university.students WHERE id = %(id)s RETURNING id" %  {'id': id}  
        conn = self.get_connection()

        row = connect_pg.execute_commands(conn, (query,))
        _userService.delete_user(student["user_id"])
        return row
    
    
    def update_student(self, id, data):
        """ Update a student record by id using data in JSON format """
        # data = request.json

        # Check if the student record with the given id exists
        existing_student = self.get_student_by_id(id)
        if not existing_student:
            return existing_student

        last_name = data.get('last_name', existing_student['last_name'])
        first_name = data.get('first_name', existing_student['first_name'])
        department_id = data.get('department_id', existing_student['department_id'])
        group_id = data.get('group_id', existing_student['group_id'])
        subgroup_id = data.get('subgroup_id', existing_student['subgroup_id'])

        query = """UPDATE university.students
                SET last_name = '%(last_name)s',
                    first_name = '%(first_name)s',
                    department_id = '%(department_id)s',
                    group_id = '%(group_id)s',
                    subgroup_id = '%(subgroup_id)s'
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'last_name': last_name,
                'first_name': first_name,
                'department_id': department_id,
                'group_id': group_id,
                'subgroup_id': subgroup_id
            }

        conn = self.get_connection()
        updated_id = connect_pg.execute_commands(conn, (query,))
        #connect_pg.disconnect(conn)

        return updated_id

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
            #connect_pg.disconnect(conn)
            return returnStatement

    def get_student_statement(self, row):
        return {
            'id': row[0],
            'last_name': row[1],         # Le nom de famille de l'étudiant
            'first_name': row[2],        # Le prénom de l'étudiant
            'user_id': row[3],      # Le numéro de téléphone de l'étudiant
            'department_id': row[4],     # L'ID du département auquel l'étudiant est affilié
            'group_id': row[5],          # L'ID du groupe auquel l'étudiant appartient
            'subgroup_id': row[6]        # L'ID du sous-groupe auquel l'étudiant est associé
        }