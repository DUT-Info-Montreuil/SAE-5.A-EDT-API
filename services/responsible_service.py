from services.main_service import Service

import connect_pg

class responsible_service(Service):
    
    # Participates API
    # university.responsibles(@id, #teaching_id, #personal_id)
    def get_responsibles(self):
        """ Get all responsibles in JSON format """
        query = "SELECT * FROM university.responsibles"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_responsible_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_responsible_by_id(self, id):
        """ Get a responsible by ID in JSON format """
        query = "SELECT * FROM university.responsibles WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_responsible_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_responsible(self, data):
        """Identify a responsible by personal_id and teaching_id in JSON format"""
        # data = request.json
        personal_id = data.get('personal_id', '')
        teaching_id = data.get('teaching_id', '')
    
        query = "SELECT * FROM university.responsibles WHERE personal_id = %(personal_id)s AND teaching_id = %(teaching_id)s" %  {'personal_id': personal_id, 'teaching_id': teaching_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_responsible_statement(row))
    
        return returnStatement
    
    def add_responsible(self, data):
        """ Add a responsible by data in JSON format """
        # data = request.json
    
        personal_id = data.get('personal_id', '')
        teaching_id = data.get('teaching_id', '')
    
        query = "INSERT INTO university.responsibles (personal_id, teaching_id) VALUES (%(personal_id)s, %(teaching_id)s) RETURNING id" % {'personal_id': personal_id, 'teaching_id': teaching_id}
        conn = self.get_connection()
        new_responsible_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_responsible_id
    
    def delete_responsible_by_id(self, id):
        """ Delete a responsible by ID in JSON format """
        query = "DELETE FROM university.responsibles WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_responsible(self, id, data):
        """ Update a responsible record by ID using data in JSON format """
        # data = request.json

        # Check if the responsible record with the given ID exists
        existing_responsible = self.get_responsible_by_id(id)
        if not existing_responsible:
            return existing_responsible

        personal_id = data.get('personal_id', existing_responsible['personal_id'])
        teaching_id = data.get('teaching_id', existing_responsible['teaching_id'])

        query = """UPDATE university.responsibles
                    SET personal_id = %(personal_id)s,
                        teaching_id = %(teaching_id)s
                    WHERE id = %(id)s
                    RETURNING id """ % {
                        'id': id,
                        'personal_id': personal_id,
                        'teaching_id': teaching_id
                    }

        conn = self.get_connection()
        updated_responsible_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_responsible_id

    
    def get_responsible_statement(self, row):
        """ Formats responsible data in JSON """
        return {
            'id': row[0],              # L'ID du cours
            'personal_id': row[1],     # L'ID du personnel associée au responsible
            'teaching_id': row[2]     # L'ID de la ressource associée au responsible
        }