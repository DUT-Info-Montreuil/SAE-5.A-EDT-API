from services.main_service import Service

from configuration import connect_pg

class reminder_service(Service):
    
    # Participates API
    # university.reminders(@id, name, description, #course_id)
    def get_reminders(self):
        """ Get all reminders in JSON format """
        query = "SELECT * FROM university.reminders"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_reminder_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_reminder_by_id(self, id):
        """ Get a reminder by ID in JSON format """
        query = "SELECT * FROM university.reminders WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_reminder_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_reminder(self, data):
        """Identify a reminder by course_id and subgroup_id in JSON format"""
        # data = request.json
        name = data.get('name', '')
        description = data.get('description', '')
        course_id = data.get('course_id', '')
        
        query = "SELECT * FROM university.reminders WHERE name = '%(name)s' AND description = '%(description)s' AND course_id = %(course_id)s" %  {'name': name, 'description': description, 'course_id': course_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_reminder_statement(row))
    
        return returnStatement
    
    def add_reminder(self, data):
        """ Add a reminder by data in JSON format """
        # data = request.json
    
        name = data.get('name', '')
        description = data.get('description', '')
        course_id = data.get('course_id', '')
        
        query = "INSERT INTO university.reminders (name, description, course_id) VALUES ('%(name)s', '%(description)s', %(course_id)s) RETURNING id" % {'name': name, 'description': description, 'course_id': course_id}
        conn = self.get_connection()
        new_reminder_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_reminder_id
    
    def delete_reminder_by_id(self, id):
        """ Delete a reminder by ID in JSON format """
        query = "DELETE FROM university.reminders WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_reminder(self, id, data):
        """ Update a reminder record by ID using data in JSON format """
        # data = request.json

        # Check if the reminder record with the given ID exists
        existing_reminder = self.get_reminder_by_id(id)
        if not existing_reminder:
            return existing_reminder

        name = data.get('name', existing_reminder['name'])
        description = data.get('description', existing_reminder['description'])
        course_id = data.get('course_id', existing_reminder['course_id'])

        query = """UPDATE university.reminders
                SET name = '%(name)s',
                    description = '%(description)s',
                    course_id = %(course_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'name': name,
                    'description': description,
                    'course_id': course_id
                }

        conn = self.get_connection()
        updated_reminder_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_reminder_id

    def get_reminder_statement(self, row):
        """ Formats reminder data in JSON """
        return {
            'id': row[0],   # L'ID du cours
            'name': row[1],     # Nom du rappel
            'description': row[2],     # Description du rappel
            'course_id': row[3]     # L'ID du cours
        }