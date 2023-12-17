
from configuration import connect_pg
from services.main_basic_service import *
class participate_service(Service):
    
    # === region : Participate ===
    def get_all_participates(self):
        participates = Participate.query.all()
        participate_list = []

        for participate in participates:
            participate_data = participate.get_json()
            participate_list.append(participate_data)

        return participate_list
    
    def get_participate_by_id(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            participate_data = participate.get_json()
            return participate_data
        else:
            return None
    
    def find_participate(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        participates = Participate.query.filter_by(**conditions)

        participate_list = []

        for participate in participates:
            participate_list.append(participate.get_json())

        return participate_list
    
    def delete_participate(self, participate_id):
        participate = Participate.query.get(participate_id)

        if participate:
            db.session.delete(participate)
            db.session.commit()
            return True
        else:
            return False
    
    def update_participate(self, participate_id, new_data):
        participate = Participate.query.get(participate_id)

        if participate:
            for key, value in new_data.items():
                setattr(participate, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_participate(self, participate_data):
        new_participate = Participate(**participate_data)

        try:
            db.session.add(new_participate)
            db.session.commit()
            return new_participate.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Participate ===

    
    # Participates API
    # university.participates(@id, justified, student_number, #course_id)
    def get_participates(self):
        """ Get all participates in JSON format """
        query = "SELECT * FROM university.participates"
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_participate_statement(row))
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def get_participate_by_id(self, id):
        """ Get a participate by ID in JSON format """
        query = "SELECT * FROM university.participates WHERE id = %(id)s" % {'id': id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        returnStatement = {}
        if len(rows) > 0:
            returnStatement = self.get_participate_statement(rows[0])
        # connect_pg.disconnect(conn)
        return returnStatement
    
    def identify_participate(self, data):
        """Identify a participate by course_id and subgroup_id in JSON format"""
        # data = request.json
        course_id = data.get('course_id', '')
        subgroup_id = data.get('subgroup_id', '')
    
        query = "SELECT * FROM university.participates WHERE course_id = %(course_id)s AND subgroup_id = %(subgroup_id)s" %  {'course_id': course_id, 'subgroup_id': subgroup_id}
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        # connect_pg.disconnect(conn)
    
        returnStatement = []
        for row in rows:
            returnStatement.append(self.get_participate_statement(row))
    
        return returnStatement
    
    def add_participate(self, data):
        """ Add a participate by data in JSON format """
        # data = request.json
    
        course_id = data.get('course_id', '')
        subgroup_id = data.get('subgroup_id', '')
    
        query = "INSERT INTO university.participates (course_id, subgroup_id) VALUES (%(course_id)s, %(subgroup_id)s) RETURNING id" % {'course_id': course_id, 'subgroup_id': subgroup_id}
        conn = self.get_connection()
        new_participate_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
    
        return new_participate_id
    
    def delete_participate_by_id(self, id):
        """ Delete a participate by ID in JSON format """
        query = "DELETE FROM university.participates WHERE id = %(id)s RETURNING id" %  {'id': id}
        conn = self.get_connection()
        row = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)
        return row
    
    def update_participate(self, id, data):
        """ Update a participate record by ID using data in JSON format """
        # data = request.json

        # Check if the participate record with the given ID exists
        existing_participate = self.get_participate_by_id(id)
        if not existing_participate:
            return existing_participate

        course_id = data.get('course_id', existing_participate['course_id'])
        rooms_id = data.get('rooms_id', existing_participate['rooms_id'])

        query = """UPDATE university.participates
                SET course_id = %(course_id)s,
                    rooms_id = %(rooms_id)s
                WHERE id = %(id)s
                RETURNING id """ % {
                    'id': id,
                    'course_id': course_id,
                    'rooms_id': rooms_id
                }

        conn = self.get_connection()
        updated_participate_id = connect_pg.execute_commands(conn, (query,))
        # connect_pg.disconnect(conn)

        return updated_participate_id
    
    def get_participate_statement(self, row):
        """ Formats participate data in JSON """
        return {
            'id': row[0],              # L'ID du cours
            'course_id': row[1],     # L'ID du subgroup associée au participate
            'rooms_id': row[2]     # L'ID du subgroup associée au participate
        }