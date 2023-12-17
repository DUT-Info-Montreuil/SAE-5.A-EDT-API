from services.main_basic_service import *
from configuration import connect_pg

class personal_service(Service):
    
    # === region : Personal ===
    def get_all_personals(self):
        personals = Personal.query.all()
        personal_list = []

        for personal in personals:
            personal_data = personal.get_json()
            personal_list.append(personal_data)

        return personal_list
    
    def get_personal_by_id(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            personal_data = personal.get_json()
            return personal_data
        else:
            return None
    
    def find_personal(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        personals = Personal.query.filter_by(**conditions)

        personal_list = []

        for personal in personals:
            personal_list.append(personal.get_json())

        return personal_list
    
    def delete_personal(self, personal_id):
        personal = Personal.query.get(personal_id)

        if personal:
            db.session.delete(personal)
            db.session.commit()
            return True
        else:
            return False
    
    def update_personal(self, personal_id, new_data):
        personal = Personal.query.get(personal_id)

        if personal:
            for key, value in new_data.items():
                setattr(personal, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_personal(self, personal_data):
        new_personal = Personal(**personal_data)

        try:
            db.session.add(new_personal)
            db.session.commit()
            return new_personal.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Personal ===

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
        # data = request.json
    
        last_name = data.get('last_name', '')
        first_name = data.get('first_name', '')
        mail = data.get('mail', '')
        phone_number = data.get('phone_number', '')
    
        query = "INSERT INTO university.personals (last_name, first_name, mail, phone_number) VALUES '(%(last_name)s', '%(first_name)s', '%(mail)s', '%(phone_number)s') RETURNING id" %  {'last_name': last_name, 'first_name': first_name, 'mail': mail, 'phone_number': phone_number}
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
        phone_number = data.get('phone_number', existing_personal['phone_number'])

        query = """UPDATE university.personals
                SET last_name = '%(last_name)s',
                    first_name = '%(first_name)s',
                    mail = '%(mail)s',
                    phone_number = '%(phone_number)'s
            WHERE id = %(id)s
            RETURNING id """ % {
                'id': id,
                'last_name': last_name,
                'first_name': first_name,
                'mail': mail,
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
            'personal_code': row[4],     # Le numéro de téléphone du personnel
            'phone_number': row[5]
        }