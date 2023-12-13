from services.main_service import Service

import connect_pg

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
        reminder_timestamp = data.get('reminder_timestamp', '')
        students_number = data.get('students_number', '')
        course_id = data.get('course_id', '')
        
        query = "SELECT * FROM university.reminders WHERE name = '%(name)s' AND description = '%(description)s' AND reminder_timestamp = '%(reminder_timestamp)s' AND students_number = '%(students_number)s' AND course_id = %(course_id)s" % {'name': name, 'description': description, 'reminder_timestamp': reminder_timestamp, 'students_number': students_number, 'course_id': course_id}
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
        reminder_timestamp = data.get('reminder_timestamp', '')
        students_number = data.get('students_number', '')
        course_id = data.get('course_id', '')
        
        query = "INSERT INTO university.reminders (name, description, reminder_timestamp, students_number, course_id) VALUES ('%(name)s', '%(description)s', '%(reminder_timestamp)s', '%(students_number)s',%(course_id)s) RETURNING id" % {'name': name, 'description': description, 'reminder_timestamp': reminder_timestamp, 'students_number': students_number, 'course_id': course_id}
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
        reminder_timestamp = data.get('reminder_timestamp', existing_reminder['reminder_timestamp'])
        students_number = data.get('students_number', existing_reminder['students_number'])
        course_id = data.get('course_id', existing_reminder['course_id'])

        query = """UPDATE university.reminders
                SET name = '%(name)s',
                    description = '%(description)s',
                    reminder_timestamp = '%(reminder_timestamp)s',
                    students_number = '%(students_number)s',
                    course_id = %(course_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'name': name,
                    'description': description,
                    'reminder_timestamp': reminder_timestamp,
                    'students_number': students_number,
                    'course_id': course_id
                }

        conn = self.get_connection()
        updated_reminder_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_reminder_id

    def get_dashboard_reminder(self, student_number, page):
        query = "SELECT * FROM university.reminders WHERE student_number = '%(student_number)s'" % {'student_number': student_number}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        rowsList = []
        for row in rows:
            rowsList.append(self.get_reminder_statement(row))

        # Tri de la liste par reminder_timestamp dans l'ordre décroissant
        sorted_list = sorted(rowsList, key=lambda x: x['reminder_timestamp'], reverse=True)

        # Calculer l'offset pour la pagination
        offset = (page - 1) * 5

        # Sélection des 5 éléments pour la page spécifiée
        returnStatement = sorted_list[offset:offset + 5]

        return returnStatement


    def get_reminder_statement(self, row):
        """ Formats reminder data in JSON """
        return {
            'id': row[0],   # L'ID du cours
            'name': row[1],     # Nom du rappel
            'description': row[2],     # Description du rappel
            'reminder_timestamp': row[3], # Heure du rappel
            'students_number': row[4],
            'course_id': row[5]     # L'ID du cours
        }