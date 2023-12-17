from services.main_service import Service

from configuration import connect_pg

class group_service(Service):
    
    # Groups API
    # university.groups(@id, promotion, type, #department_id)
    def get_groups(self):
        """ Get all groups in JSON format """
        query = "SELECT * FROM university.groups"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_group_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_group_by_id(self, id):
        """ Get a group by ID in JSON format """
        query = "SELECT * FROM university.groups WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_group_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_group(self, data):
        """Identify a group by promotion and type in JSON format"""
        # data = request.json
        
        promotion = data.get('promotion', '')
        group_type = data.get('type', '')
        department_id = data.get('department_id', '')
    
        query = "SELECT * FROM university.groups WHERE promotion = %(promotion)s AND type = '%(type)s' AND department_id = %(department_id)s" %  {'promotion': promotion, 'type': group_type, 'department_id': department_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_group_statement(row))
    
        return returnStatement
    
    def add_group(self, data):
        """ Add a group by data in JSON format """
        # data = request.json
    
        promotion = data.get('promotion', '')
        group_type = data.get('type', '')
        department_id = data.get('department_id', '')
    
        query = "INSERT INTO university.groups (promotion, type, department_id) VALUES (%(promotion)s, '%(type)s', %(department_id)s) RETURNING id" % {'promotion': promotion, 'type': group_type, 'department_id': department_id}
        conn = self.get_connection()
        new_group_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_group_id
    
    def delete_group_by_id(self, id):
        """ Delete a group by ID in JSON format """
        query = "DELETE FROM university.groups WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_group(self, id, data):
        """ Update a group record by ID using data in JSON format """
        # data = request.json

        # Check if the group record with the given ID exists
        existing_group = self.get_group_by_id(id)
        if not existing_group:
            return existing_group

        promotion = data.get('promotion', existing_group['promotion'])
        type = data.get('type', existing_group['type'])
        department_id = data.get('department_id', existing_group['department_id'])

        query = """UPDATE university.groups
                SET promotion = %(promotion)s,
                    type = '%(type)s',
                    department_id = %(department_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'promotion': promotion,
                    'type': type,
                    'department_id': department_id
                }

        conn = self.get_connection()
        updated_group_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_group_id

    def get_group_statement(self, row):
        """ Formats group data in JSON"""
        return {
            'id': row[0],              # L'ID du groupe
            'promotion': row[1],       # La promotion du groupe
            'type': row[2],            # Le type du groupe
            'department_id': row[3]    # L'ID du département associé au groupe
        }