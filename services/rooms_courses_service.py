from services.main_service import Service

from configuration import connect_pg

class rooms_courses_service(Service):
    
    # rooms_courses API
    # university.roles(@id, name, description, personal_id)
    def get_rooms_courses(self):
        """ Get all rooms_courses in JSON format """
        query = "SELECT * FROM university.rooms_courses"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_rooms_courses_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_rooms_courses_by_id(self, id):
        """ Get a rooms_courses by ID in JSON format """
        query = "SELECT * FROM university.rooms_courses WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_rooms_courses_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def add_rooms_courses(self, data):
        """ Add a rooms_courses by data in JSON format """
        # data = request.json
    
        course_id = data.get('course_id', '')
        rooms_id = data.get('rooms_id', '')
    
        query = "INSERT INTO university.rooms_courses (course_id, rooms_id) VALUES ('%(course_id)s', '%(rooms_id)s') RETURNING id" % {'course_id': course_id, 'rooms_id': rooms_id}
        conn = self.get_connection()
        new_rooms_courses_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_rooms_courses_id
    
    def delete_rooms_courses_by_id(self, id):
        """ Delete a rooms_courses by ID in JSON format """
        query = "DELETE FROM university.rooms_courses WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_rooms_courses(self, id, data):
        """ Update a rooms_courses record by ID using data in JSON format """
        # data = request.json

        # Check if the rooms_courses record with the given ID exists
        existing_rooms_courses = self.get_rooms_courses_by_id(id)
        if not existing_rooms_courses:
            return existing_rooms_courses

        course_id = data.get('course_id', existing_rooms_courses['course_id'])
        rooms_id = data.get('rooms_id', existing_rooms_courses['rooms_id'])

        query = """UPDATE university.rooms_courses
                SET course_id = '%(course_id)s',
                    rooms_id = %(rooms_id)s,                
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'course_id': course_id,
                    'rooms_id': rooms_id
                    
                }

        conn = self.get_connection()
        updated_rooms_courses_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_rooms_courses_id

    
    def get_rooms_courses_statement(self, row):
        """ Formats rooms_courses data in JSON """
        return {
            'id': row[0],              # L'ID de la salle
            'course_id': row[1],       # ID du cours
            'rooms_id': row[2]        # ID de la salle
        }