from services.main_service import Service

import connect_pg

class user_service(Service):

    def add_user(self, data):
        username = data.get('username', '')
        #do the hashing
        password = data.get('password', '')

        if username == '' or password == '':
            return 'Null arguments'
        if len(username) > 64:
            return 'username to long'
        
        query = "INSERT INTO university.users (username, password) VALUES ('" + username + "', '" + password + "')"

        conn = self.get_connection()
        connect_pg.execute_commands(conn, (query,))
        connect_pg.disconnect(conn)

        return "Successfully inserted"

        
    
