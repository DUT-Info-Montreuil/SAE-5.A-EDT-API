from services.main_service import Service
import connect_pg

class department_service(Service):
    # Departments API
    # university.departments(@id, name, description, department_type)
    def get_departments(self):
        """ Get all department in JSON format """
        query = "SELECT * FROM university.departments"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_department_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_department_by_id(self, id):
        """ Get a department by ID in JSON format """
        query = "SELECT * FROM university.departments WHERE id = %(id)s" %  {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_department_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_department(self, data):
        """Identify a department by name and degree_type in JSON format"""
        # data = request.json
        name = data.get('name', '')
        degree_type = data.get('degree_type', '')
    
        query = "SELECT * FROM university.departments WHERE name = '%(name)s' AND degree_type = '%(degree_type)s'" % {'name': name, 'degree_type': degree_type}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_department_statement(row))
    
        return returnStatement
    
    def add_department(self, data):
        """ Add a department by data in JSON format """
        # data = request.json
    
        name = data.get('name', '')
        description = data.get('description', '')
        degree_type = data.get('degree_type', '')
        personal_id = data.get('personal_id', '')
    
        query = "INSERT INTO university.departments (name, description, degree_type, personal_id) VALUES ('%(name)s', '%(description)s', '%(degree_type)s', %(personal_id)s) RETURNING id" %  {'name': name, 'description': description, 'degree_type': degree_type, 'personal_id': personal_id}
        conn = self.get_connection()
        new_department_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return new_department_id
    
    def delete_department_by_id(self, id):
        """ Delete a department by ID in JSON format """
        query = "DELETE FROM university.departments WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        print(row)
        return row
    
    def update_department(self, id, data):
        """ Update a department record by ID using data in JSON format """
        # data = request.json

        # Check if the department record with the given ID exists
        existing_department = self.get_department_by_id(id)
        if not existing_department:
            return existing_department

        name = data.get('name', existing_department['name'])
        description = data.get('description', existing_department['description'])
        degree_type = data.get('degree_type', existing_department['degree_type'])
        personal_id = data.get('personal_id', existing_department['personal_id'])

        query = """UPDATE university.departments
                    SET name = '%(name)s',
                    description = '%(description)s',
                    degree_type = '%(degree_type)s',
                    personal_id = %(personal_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                'id': id,
                'name': name,
                'description': description,
                'degree_type': degree_type,
                'personal_id': personal_id
            }
        
        conn = self.get_connection()
        updated_department_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_department_id

    
    def get_department_statement(self, row):
        """ Formats department data in JSON"""
        return {
            'id': row[0],              # L'ID du département
            'name': row[1],            # Le nom du département
            'description': row[2],     # La description du département
            'degree_type': row[3],     # Le type de diplôme du département
            'personal_id': row[4]      # L'ID du personnel associé au département
        }