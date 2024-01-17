from services.main_service import Service

from configuration import connect_pg

class absent_service(Service):
    
    # university.absents(@id, justified, student_number, #course_id)

    # ----------------------------------------------------------
    # Recuperer data
    # ----------------------------------------------------------

    def get_absents(self):
        """ Get all absents in JSON format """
        query = "SELECT * FROM university.absents"
        return self.execute_query_and_get_statement(query)
    
    def get_absent_by_id(self, id):
        """ Get a absent by ID in JSON format """
        query = "SELECT * FROM university.absents WHERE id = " + str(id)
        returnStatement = self.execute_query_and_get_statement(query)
        if len(returnStatement) == 1:
            return returnStatement
        else:
            return {}
    
    # ----------------------------------------------------------
    # Add / Delete / Update
    # ----------------------------------------------------------
    
    def add_absent(self, data):
        """ Add a absent by data in JSON format """
        justified = data.get('justified', '')
        student_number = data.get('student_number', '')
        course_id = data.get('course_id', '')
    
        query = "INSERT INTO university.absents (justified, student_number, course_id) VALUES ('" + justified + "', '" + student_number + "', " + course_id + ")"
        conn = self.get_connection()
        new_absent_id = connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)
    
        return new_absent_id
    
    def delete_absent_by_id(self, id):
        """ Delete a absent by ID in JSON format """
        query = "DELETE FROM university.absents WHERE id = " + str(id)
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_absent(self, id, data):
        """ Update an absent record by ID using data in JSON format """
        sub_query = ''
        justified = data.get('justified', '')
        student_number = data.get('student_number', '')
        course_id = data.get('course_id', '')

        if justified != '':
            sub_query = sub_query + """justified = '""" + str(justified) + """' """
        if student_number != '':
            sub_query = sub_query + """student_number = '""" + str(student_number) + """' """
        if course_id != '':
            sub_query = sub_query + """justified = """ + str(course_id) + """ """
        
        # @TO-DO: add other attributes
        if sub_query == '':
            return {"message": "Invalid arguments"}
        
        query = """UPDATE university.absents SET """ + sub_query + """ WHERE id = """ + str(id)
        try:
            conn = self.get_connection()
            connect_pg.execute_commands(conn, (query,))
            connect_pg.disconnect(conn)
            return {"message": "Course " + str(id) + " updated sucessfully"}
        except Exception as e:
            return  {"message": e}

    # ----------------------------------------------------------
    # Utilitaires
    # ----------------------------------------------------------
    
    def execute_query_and_get_statement(self, query):
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_absent_statement(row))
        connect_pg.disconnect(conn)
        return returnStatement

    def get_absent_statement(self, row):
        """ Formats absent data in JSON """
        return {
            'id': row[0],              # L'ID de l'absent
            'justified': row[1],     # La justification (t ou f)
            'student_number': row[2],       # Le numero etudiant de l'absent
            'course_id': row[3],           # L'ID du cours
        }