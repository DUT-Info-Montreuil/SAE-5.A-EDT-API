from services.main_service import Service

from configuration import connect_pg

from services.user_service import UserService

class personal_service(Service):
    

    ## stat

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
    # university.personals(@id, last_name, first_name, mail, phone_number)
    def get_personals(self):
        """ Get all personals in JSON format """
        query = "SELECT * FROM university.personals"
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
    
    def identify_personal(self, data):
        """Identify a personal by mail in JSON format"""
        # data = request.json
        mail = data.get('mail', '')
    
        query = "SELECT * FROM university.personals WHERE mail = '%(mail)s'" % {'mail': mail}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn,query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_personal_statement(row))
    
        return returnStatement
    
    def add_personal(self, data):
        """ Add a personal by data in JSON format """
        _userService = UserService()

        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
        personal_code = data.get('personal_code', '')

        userData = {
            "username": data["first_name"][0].lower() + data["last_name"].lower(),
            "password": data["password"]
        }

        new_user_id = _userService.add_user(userData)
    
        query = "INSERT INTO university.personals (last_name, first_name, mail, personal_code, user_id, phone_number) VALUES ('%(last_name)s', '%(first_name)s', '%(mail)s', '%(personal_code)s','%(new_user_id)s', '%(phone_number)s') RETURNING id" %  {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'personal_code': personal_code, 'new_user_id': new_user_id, 'phone_number': phone_number}
        conn = self.get_connection()
        new_personal_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_personal_id
    
    def delete_personal_by_id(self, id):
        """ Delete a personal by ID in JSON format """
        query = "DELETE FROM university.personals WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
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
        mail = data.get('mail', existing_personal['mail'])
        personal_code = data.get('personal_code', existing_personal['personal_code'])
        user_id = data.get('user_id', existing_personal['user_id'])
        phone_number = data.get('phone_number', existing_personal['phone_number'])

        query = """UPDATE university.personals
                SET last_name = '%(last_name)s',
                    first_name = '%(first_name)s',
                    mail = '%(mail)s',
                    personal_code = '%(personal_code)s',
                    user_id = '%(user_id)s',
                    phone_number = '%(phone_number)s'
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'last_name': last_name,
                'first_name': first_name,
                'mail': mail,
                'personal_code': personal_code,
                'user_id': user_id,
                'phone_number': phone_number
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
            'mail': row[3],            # L'adresse e-mail du personnel
            'personal_code': row[4],
            'user_id': row[5],  
            'phone_number': row[6] # Le numéro de téléphone du personnel
        }
    


    