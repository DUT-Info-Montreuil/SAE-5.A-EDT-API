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
    
    
    def get_dashboard_absents(self, student_number, page):
        """   """
        query = "SELECT * FROM university.absents WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)


        if len(rows) > 0 :     
            returnStatement = []
            for row in rows:
                student_number = row[2]
                courses_id = row[3]

                query_student = "SELECT last_name, first_name FROM university.students WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
                rows_student = connect_pg.get_query(conn, query_student)  

                return_rows_student = {
                    'first_name': rows_student[0][0],
                    'last_name': rows_student[0][1]
                }

                query_courses = "SELECT starttime, endtime, course_type, teaching_id FROM university.courses WHERE id = %(id)s" % {'id': courses_id}
                rows_courses = connect_pg.get_query(conn, query_courses)   

                return_rows_courses = {
                    'starttime': rows_courses[0][0],
                    'endtime': rows_courses[0][1],
                    'course_type': rows_courses[0][2],
                    'teaching_id': rows_courses[0][3],
                    'duration_minutes': (rows_courses[0][1] - rows_courses[0][0]).total_seconds() /60
                }


                teaching_id = rows_courses[0][3]

                query_teaching = "SELECT title FROM university.teachings WHERE id = %(id)s" % {'id': teaching_id}
                rows_teaching = connect_pg.get_query(conn, query_teaching)   

                return_rows_teaching = {
                    'title': rows_teaching[0][0]
                }
                return_rows_absent = self.get_absent_statement(row)
                row_statement = {**return_rows_absent, **return_rows_student, **return_rows_courses, **return_rows_teaching}
                returnStatement.append(row_statement)

        return returnStatement
    
    
    def get_absent_statement(self, row):
        """ Formats absent data in JSON """
        return {
            'id': row[0],              # L'ID de l'absent
            'justified': row[1],     # La justification (t ou f)
            'student_number': row[2],       # Le numero etudiant de l'absent
            'course_id': row[3],           # L'ID du cours
        }