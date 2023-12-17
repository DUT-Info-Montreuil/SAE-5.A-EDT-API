
from configuration import connect_pg
from services.main_basic_service import *
class group_service(Service):
    
    # === region : Group ===
    def get_all_groups(self):
        groups = Group.query.all()
        group_list = []

        for group in groups:
            group_data = group.get_json()
            group_list.append(group_data)

        return group_list
    
    def get_group_by_id(self, group_id):
        group = Group.query.get(group_id)

        if group:
            group_data = group.get_json()
            return group_data
        else:
            return None
    
    def find_group(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        groups = Group.query.filter_by(**conditions)

        group_list = []

        for group in groups:
            group_list.append(group.get_json())

        return group_list
    
    def delete_group(self, group_id):
        group = Group.query.get(group_id)

        if group:
            db.session.delete(group)
            db.session.commit()
            return True
        else:
            return False
    
    def update_group(self, group_id, new_data):
        group = Group.query.get(group_id)

        if group:
            for key, value in new_data.items():
                setattr(group, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_group(self, group_data):
        new_group = Group(**group_data)

        try:
            db.session.add(new_group)
            db.session.commit()
            return new_group.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Group ===

    
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
        department_id = data.get('department_id', '')
    
        query = "SELECT * FROM university.groups WHERE promotion = '" + promotion + "' AND department_id = '" + department_id + "'"
        print(query)
        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)
        connect_pg.disconnect(conn)
    
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