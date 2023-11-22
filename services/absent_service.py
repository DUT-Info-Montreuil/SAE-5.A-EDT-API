from services.main_service import Service

import connect_pg

class absent_service(Service):
    
    # Absents API
    # university.absents(@id, justified, student_number, #course_id)
    def get_absents(self):
        """ Get all absents in JSON format """
        query = "SELECT * FROM university.absents"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_absent_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_absent_by_id(self, id):
        """ Get a absent by ID in JSON format """
        query = "SELECT * FROM university.absents WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_absent_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_absent(self, data):
        """Identify a absent by justified, student_number and course_id in JSON format"""
        # data = request.json

        justified = data.get('justified', '')
        student_number = data.get('student_number', '')
        course_id = data.get('course_id', '')
    
        query = "SELECT * FROM university.absents WHERE justified = '%(justified)s' AND student_number = '%(student_number)s' AND course_id = %(course_id)s" %  {'justified': justified, 'student_number': student_number, 'course_id': course_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_absent_statement(row))
    
        return returnStatement
    
    def add_absent(self, data):
        """ Add a absent by data in JSON format """
        # data = request.json
    
        justified = data.get('justified', '')
        student_number = data.get('student_number', '')
        course_id = data.get('course_id', '')
    
        query = "INSERT INTO university.absents (justified, student_number, course_id) VALUES ('%(justified)s', '%(student_number)s', %(course_id)s) RETURNING id" % {'justified': justified, 'student_number': student_number, 'course_id': course_id}
        conn = self.get_connection()
        new_absent_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_absent_id
    
    def delete_absent_by_id(self, id):
        """ Delete a absent by ID in JSON format """
        query = "DELETE FROM university.absents WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_absent(self, id, data):
        """ Update an absent record by ID using data in JSON format """
        # data = request.json

        # Check if the absent record with the given ID exists
        existing_absent = self.get_absent_by_id(id)
        if not existing_absent:
            return existing_absent

        justified = data.get('justified', existing_absent['justified'])
        student_number = data.get('student_number', existing_absent['student_number'])
        course_id = data.get('course_id', existing_absent['course_id'])

        query = """UPDATE university.absents
                SET justified = '%(justified)s',
                student_number = '%(student_number)s',
                course_id = %(course_id)s
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'justified': justified,
                'student_number': student_number,
                'course_id': course_id
            }

        conn = self.get_connection()
        updated_absent_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_absent_id

    
    def get_absent_statement(self, row):
        """ Formats absent data in JSON """
        return {
            'id': row[0],              # L'ID de l'absent
            'justified': row[1],     # La justification (t ou f)
            'student_number': row[2],       # Le numero etudiant de l'absent
            'course_id': row[3],           # L'ID du cours
        }