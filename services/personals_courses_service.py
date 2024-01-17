from services.main_service import Service

from configuration import connect_pg

class personals_courses_service(Service):
    
    # personals_courses API
    # university.roles(@id, name, description, personal_id)
    def get_personals_courses(self):
        """ Get all personals_courses in JSON format """
        query = "SELECT * FROM university.personals_courses"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_personals_courses_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_personals_courses_by_id(self, id):
        """ Get a personals_courses by ID in JSON format """
        query = "SELECT * FROM university.personals_courses WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_personals_courses_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def add_personals_courses(self, data):
        """ Add a personals_courses by data in JSON format """
        # data = request.json
    
        course_id = data.get('course_id', '')
        personal_id = data.get('personal_id', '')
    
        query = "INSERT INTO university.personals_courses (course_id, personal_id) VALUES ('%(course_id)s', '%(personal_id)s') RETURNING id" % {'course_id': course_id, 'personal_id': personal_id}
        conn = self.get_connection()
        new_personals_courses_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_personals_courses_id
    
    def delete_personals_courses_by_id(self, id):
        """ Delete a personals_courses by ID in JSON format """
        query = "DELETE FROM university.personals_courses WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_personals_courses(self, id, data):
        """ Update a personals_courses record by ID using data in JSON format """
        # data = request.json

        # Check if the personals_courses record with the given ID exists
        existing_personals_courses = self.get_personals_courses_by_id(id)
        if not existing_personals_courses:
            return existing_personals_courses

        course_id = data.get('course_id', existing_personals_courses['course_id'])
        personal_id = data.get('personal_id', existing_personals_courses['personal_id'])

        query = """UPDATE university.personals_courses
                SET course_id = '%(course_id)s',
                    personal_id = %(personal_id)s,                
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'course_id': course_id,
                    'personal_id': personal_id
                    
                }

        conn = self.get_connection()
        updated_personals_courses_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_personals_courses_id

    
    def get_personals_courses_statement(self, row):
        """ Formats personals_courses data in JSON """
        return {
            'id': row[0],              # L'ID de la salle
            'course_id': row[1],       # ID du cours
            'personal_id': row[2]        # ID du professeur
        }