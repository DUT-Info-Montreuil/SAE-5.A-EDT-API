from services.main_service import Service

from configuration import connect_pg

class teaching_service(Service):
    
    # Teachings API
    # university.teachings(@id, title, hour_number, semestre, sequence, description, teaching_type, #specialization_id)
    def get_teachings(self):
        """ Get all teachings in JSON format """
        query = "SELECT * FROM university.teachings"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_teaching_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_teaching_by_id(self, id):
        """ Get a teaching by ID in JSON format """
        query = "SELECT * FROM university.teachings WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_teaching_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_teaching(self, data):
        """Identify a teaching by title, hour_number, semestre, sequence, and specialization_id in JSON format"""
        # data = request.json
        title = data.get('title', '')
        hour_number = data.get('hour_number', '')
        semestre = data.get('semestre', '')
        sequence = data.get('sequence', '')
        specialization_id = data.get('specialization_id', '')
    
        query = "SELECT * FROM university.teachings WHERE title = '%(title)s' AND hour_number = %(hour_number)s AND semestre = %(semestre)s AND sequence = '%(sequence)s' AND specialization_id = %(specialization_id)s" % {'title': title, 'hour_number': hour_number, 'semestre': semestre, 'sequence': sequence, 'specialization_id': specialization_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_teaching_statement(row))
    
        return returnStatement
    
    def add_teaching(self, data):
        """ Add a teaching by data in JSON format """
        # data = request.json
    
        title = data.get('title', '')
        hour_number = data.get('hour_number', '')
        semestre = data.get('semestre', '')
        sequence = data.get('sequence', '')
        description = data.get('description', '')
        teaching_type = data.get('teaching_type', '')
        specialization_id = data.get('specialization_id', '')
    
        query = "INSERT INTO university.teachings (title, hour_number, semestre, sequence, description, teaching_type, specialization_id) VALUES ('%(title)s', %(hour_number)s, %(semestre)s, '%(sequence)s', '%(description)s', '%(teaching_type)s,' %(specialization_id)s) RETURNING id" % {'title': title, 'hour_number': hour_number, 'semestre': semestre, 'sequence': sequence, 'description': description, 'teaching_type': teaching_type, 'specialization_id': specialization_id}
        conn = self.get_connection()
        new_teaching_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_teaching_id
    
    def delete_teaching_by_id(self, id):
        """ Delete a teaching by ID in JSON format """
        query = "DELETE FROM university.teachings WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_teaching(self, id, data):
        """ Update a teaching record by ID using data in JSON format """
        # data = request.json

        # Check if the teaching record with the given ID exists
        existing_teaching = self.get_teaching_by_id(id)
        if not existing_teaching:
            return existing_teaching

        title = data.get('title', existing_teaching['title'])
        hour_number = data.get('hour_number', existing_teaching['hour_number'])
        semestre = data.get('semestre', existing_teaching['semestre'])
        sequence = data.get('sequence', existing_teaching['sequence'])
        description = data.get('description', existing_teaching['description'])
        teaching_type = data.get('teaching_type', existing_teaching['teaching_type'])
        specialization_id = data.get('specialization_id', existing_teaching['specialization_id'])

        query = """UPDATE university.teachings
                SET title = '%(title)s',
                    hour_number = %(hour_number)s,
                    semestre = %(semestre)s,
                    sequence = '%(sequence)s',
                    description = '%(description)s',
                    teaching_type = '%(teaching_type)s',
                    specialization_id = %(specialization_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'title': title,
                    'hour_number': hour_number,
                    'semestre': semestre,
                    'sequence': sequence,
                    'description': description,
                    'teaching_type': teaching_type,
                    'specialization_id': specialization_id
                }

        conn = self.get_connection()
        updated_teaching_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_teaching_id


    def get_teaching_statement(self, row):
        """ Formats teaching data in JSON """
        return {
            'id': row[0],                   # L'ID de l'enseignement
            'title': row[1],                # Le titre de l'enseignement
            'hour_number': row[2],          # Le nombre d'heures
            'semestre': row[3],             # Le semestre
            'sequence': row[4],             # La séquence
            'description': row[5],          # La description
            'teaching_type': row[6],        # Le type d'enseignement
            'specialization_id': row[7]     # L'ID de la spécialisation associée à l'enseignement
        }