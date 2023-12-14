from services.main_service import Service

from configuration import connect_pg

class role_service(Service):
    
    # Roles API
    # roles(@id, name, description, personal_id)
    def get_roles(self):
        """ Get all roles in JSON format """
        query = "SELECT * FROM roles"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_role_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_role_by_id(self, id):
        """ Get a role by ID in JSON format """
        query = "SELECT * FROM roles WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_role_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_role(self, data):
        """Identify a role by name, and personal_id in JSON format"""
        # data = request.json
        name = data.get('name', '')
        personal_id = data.get('personal_id', '')
    
        query = "SELECT * FROM roles WHERE name = '%(name)s' AND personal_id = %(personal_id)s" %  {'name': name, 'personal_id': personal_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn,query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_role_statement(row))
    
        return returnStatement
    
    def add_role(self, data):
        """ Add a role by data in JSON format """
        # data = request.json
    
        name = data.get('name', '')
        description = data.get('description', '')
        personal_id = data.get('personal_id', '')
    
        query = "INSERT INTO roles (name, description, personal_id) VALUES ('%(name)s', '%(description)s', %(personal_id)s) RETURNING id" %  {'name': name, 'description': description, 'personal_id': personal_id}
        conn = self.get_connection()
        new_role_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_role_id
    
    def delete_role_by_id(self, id):
        """ Delete a role by ID in JSON format """
        query = "DELETE FROM roles WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_role(self, id, data):
        """ Update a role record by ID using data in JSON format """
        # data = request.json

        # Check if the role record with the given ID exists
        existing_role = self.get_role_by_id(id)
        if not existing_role:
            return existing_role

        name = data.get('name', existing_role['name'])
        description = data.get('description', existing_role['description'])
        personal_id = data.get('personal_id', existing_role['personal_id'])

        query = """UPDATE roles
                    SET name = '%(name)s',
                        description = '%(description)s',
                        personal_id = %(personal_id)s
                    WHERE id = %(id)s
                    RETURNING id """ % {
                        'id': id,
                        'name': name,
                        'description': description,
                        'personal_id': personal_id
                    }

        conn = self.get_connection()
        updated_role_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_role_id

    
    def get_role_statement(self, row):
        """ Formats role data in JSON """
        return {
            'id': row[0],              # L'ID du rôle
            'name': row[1],            # Le nom du rôle
            'description': row[2],     # La description du rôle
            'personal_id': row[3]      # L'ID du personnel associé au rôle
        }