from services.main_service import Service

from configuration import connect_pg
 
from services.user_service import UserService

class personal_service(Service):
    ## stat
    def get_roles(self, data):
        username = data.get('username', '') 
        
        if username == '':
            return {'error': 'Null arguments'}
        query = """
        SELECT 
            CASE 
                WHEN students.id IS NOT NULL THEN 'student'
                WHEN personals.id IS NOT NULL THEN personals.roles
                ELSE 'unknown'
            END as user_type
        FROM 
            university.users
        LEFT JOIN 
            university.students ON users.id = students.user_id
        LEFT JOIN 
            university.personals ON users.id = personals.user_id
        WHERE 
            users.username = '""" + username + """';"""
        
        conn = self.get_connection()
        
        rows = connect_pg.get_query(conn, query)
        if not rows:
            return None
        return {"role": rows[0][0]}
    
    def total_hours(self, id):
        """Identify a course by description, starttime, duree, course_type, personal_id, and rooms_id in JSON format"""
        # data = request.json
        #Rajouter condition, matière toussa
        query = "SELECT SUM(endtime-starttime) FROM university.courses WHERE personal_id = " + str(id)
        print(query)
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        if rows[0][0] is None:
            return {}
        connect_pg.disconnect(conn)
        return { "temps": rows[0][0].total_seconds()  / 60 }

    # Personals API
    # university.personals(@id, last_name, first_name)
    def get_personals(self):
        """ Get all personals in JSON format """
        query = 'SELECT * FROM university.personals'
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []

        for row in rows:
            returnStatement.append(self.get_personal_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_personal_by_id(self, id):
        """ Get a personal by ID in JSON format """
        query = "SELECT * FROM university.personals WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_personal_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def add_personal(self, data):
        """ Add a personal by data in JSON format """
        _userService = UserService()

        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        personal_code = data.get('personal_code', '')

        userData = {
            "username": data["first_name"][0].lower() + data["last_name"].lower(),
            "password": data["password"]
        }

        new_user_id = _userService.add_user(userData)
    
        query = "INSERT INTO university.personals (last_name, first_name, personal_code, user_id) VALUES ('%(last_name)s', '%(first_name)s', '%(personal_code)s','%(new_user_id)s') RETURNING id" %  {'last_name': last_name, 'first_name': first_name, 'personal_code': personal_code, 'new_user_id': new_user_id}
        conn = self.get_connection()
        new_personal_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_personal_id
    
    def delete_personal_by_id(self, id):
        """ Delete a personal by ID in JSON format """

        _userService = UserService()
        personal = self.get_personal_by_id(id)
        
        query = "DELETE FROM university.personals WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()

        row = connect_pg.execute_commands(conn, (query,))
        _userService.delete_user(personal["user_id"])

        return row
    
    def update_personal(self, id, data):
        """ Update a personal record by ID using data in JSON format """
        # data = request.json
        
        # Check if the personal record with the given ID exists
        existing_personal = self.get_personal_by_id(id)
        if not existing_personal:
            return existing_personal
        
        last_name = data.get('last_name', existing_personal['last_name'])
        first_name = data.get('first_name', existing_personal['first_name'])
        personal_code = data.get('personal_code', existing_personal['personal_code'])
        roles = data.get('roles', existing_personal['roles'])
        user_id = data.get('user_id', existing_personal['user_id'])

        query = """UPDATE university.personals
                SET last_name = '%(last_name)s',
                    first_name = '%(first_name)s',
                    personal_code = '%(personal_code)s',
                    roles = '%(roles)s',
                    user_id = '%(user_id)s'
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'last_name': last_name,
                'first_name': first_name,
                'personal_code': personal_code,
                'roles': roles,
                'user_id': user_id
            }
        conn = self.get_connection()
        updated_personal_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_personal_id

    
    def get_personal_statement(self, row):
        """ Formats personal data in JSON """
        return {
            'id': row[0],              # L'ID du personnel
            'last_name': row[1],       # Le nom de famille du personnel
            'first_name': row[2],      # Le prénom du personnel
            'personal_code': row[3],
            'roles': row[4],           # Le code personnel du personnel
            'user_id': row[5]
        }