from services.main_service import Service
from datetime import datetime, timedelta


import connect_pg

class course_service(Service):
    
    def get_next_courses2(self, student_number):
        current_datetime = datetime.now()
        formatted_starttime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        # Calculer la date du jour suivant
        next_day = current_datetime + timedelta(days=1)
        formatted_next_day = next_day.strftime('%Y-%m-%d 00:00:00')

        query = "SELECT * FROM university.courses WHERE starttime > %(formatted_starttime)s AND starttime < %(formatted_next_day)s"
        params = {'formatted_starttime': formatted_starttime, 'formatted_next_day': formatted_next_day}

        conn = self.get_connection()
        rows_courses = connect_pg.get_query(conn, query, params)

        returnStatement = []
        for row in rows_courses:
            returnStatement.append(self.get_course_statement(row))

        # connect_pg.disconnect(conn)
        return returnStatement

    # Courses API
    # university.courses(@id, description, starttime, endtime, course_type, #personal_id, #rooms_id, #teaching_id)
    def get_courses(self):
        """ Get all courses in JSON format """
        query = "SELECT * FROM university.courses"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_course_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_course_by_id(self, id):
        """ Get a course by ID in JSON format """
        query = "SELECT * FROM university.courses WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_course_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_course(self, data):
        """Identify a course by description, starttime, endtime, course_type, personal_id, and rooms_id in JSON format"""
        # data = request.json

        starttime = data.get('starttime', '')
        teaching_id = data.get('teaching_id', '')
        personal_id = data.get('personal_id', '')
        rooms_id = data.get('rooms_id', '')
    
        query = "SELECT * FROM university.courses WHERE starttime = '%(starttime)s' AND teaching_id = %(teaching_id)s AND personal_id = %(personal_id)s AND rooms_id = %(rooms_id)s" %  {'starttime': starttime, 'personal_id': personal_id,'teaching_id': teaching_id, 'rooms_id': rooms_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_course_statement(row))
    
        return returnStatement
    
    def add_course(self, data):
        """ Add a course by data in JSON format """
        # data = request.json
    
        description = data.get('description', '')
        starttime = data.get('starttime', '')
        endtime = data.get('endtime', '')
        course_type = data.get('course_type', '')
        personal_id = data.get('personal_id', '')
        rooms_id = data.get('rooms_id', '')
        teaching_id = data.get('teaching_id', '')
    
        query = "INSERT INTO university.courses (description, starttime, endtime, course_type, personal_id, rooms_id, teaching_id) VALUES ('%(description)s', '%(starttime)s', '%(endtime)s', '%(course_type)s', %(personal_id)s, %(rooms_id)s, %(teaching_id)s) RETURNING id" % {'description': description, 'starttime': starttime, 'endtime': endtime, 'course_type': course_type, 'personal_id': personal_id, 'rooms_id': rooms_id, 'teaching_id': teaching_id}
        conn = self.get_connection()
        new_course_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_course_id
    
    def delete_course_by_id(self, id):
        """ Delete a course by ID in JSON format """
        query = "DELETE FROM university.courses WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_course(self, id, data):
        """ Update a course by ID using data in JSON format """
        # data = request.json

        # Check if the course with the given ID exists
        existing_course = self.get_course_by_id(id)
        if not existing_course:
            return existing_course

        description = data.get('description', existing_course['description'])
        starttime = data.get('starttime', existing_course['starttime'])
        endtime = data.get('endtime', existing_course['endtime'])
        course_type = data.get('course_type', existing_course['course_type'])
        personal_id = data.get('personal_id', existing_course['personal_id'])
        rooms_id = data.get('rooms_id', existing_course['rooms_id'])
        teaching_id = data.get('teaching_id', existing_course['teaching_id'])

        query = """UPDATE university.courses
                SET description = '%(description)s',
                starttime = '%(starttime)s',
                endtime = %(endtime)s,
                course_type = '%(course_type)s',
                personal_id = %(personal_id)s,
                rooms_id = %(rooms_id)s,
                teaching_id = %(teaching_id)s
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'description': description,
                'starttime': starttime,
                'endtime': endtime,
                'course_type': course_type,
                'personal_id': personal_id,
                'rooms_id': rooms_id,
                'teaching_id': teaching_id
            }

        conn = self.get_connection()
        updated_course_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_course_id

    def get_next_courses(self, student_number):
            # La date du jour
            current_datetime = datetime.now()
            formatted_starttime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

            # Calculer la date du jour suivant
            next_day = current_datetime + timedelta(days=1)
            formatted_next_day = next_day.strftime('%Y-%m-%d 00:00:00')

            query = "SELECT * FROM university.courses WHERE starttime > '%(formatted_starttime)s' AND starttime < '%(formatted_next_day)s'" % {'formatted_starttime': formatted_starttime, 'formatted_next_day': formatted_next_day}

            conn = self.get_connection()
            rows_courses = connect_pg.get_query(conn, query)

            returnStatement = []
            for row in rows_courses:
                returnStatement.append(self.get_course_statement(row))
            # connect_pg.disconnect(conn)

            return returnStatement
    
    def get_course_statement(self, row):
        """ Formats course data in JSON """
        return {
            'id': row[0],              # L'ID du cours
            'description': row[1],     # La description du cours
            'starttime': row[2],       # L'heure de début du cours
            'endtime': row[3],           # La durée du cours
            'course_type': row[4],     # Le type de cours
            'personal_id': row[5],     # L'ID du personnel associé au cours
            'rooms_id': row[6],        # L'ID de la salle associée au cours
            'teaching_id': row[7]      # L'ID de l'enseignement associé au cours
        }