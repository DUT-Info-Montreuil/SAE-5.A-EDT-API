from services.main_service import Service

import connect_pg
import bcrypt

class auth_service(Service):

    def login(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        if username == '' or password == '':
            return 'Username or password not filled'
        
        #password = self.hash_password(password)

        query = f"SELECT username, password FROM university.users WHERE username = '{username}';"

        conn = self.get_connection()
        rows = connect_pg.get_query(conn, query)

        if len(rows) == 0:
            return "Bad username or password"
        
        password = password.encode('utf-8') 
        dbHashedPassword = rows[0][1].encode('utf-8')
        result = bcrypt.checkpw(password, dbHashedPassword) 

        if not result:
            return "Bad username or password"
        
        connect_pg.disconnect(conn)
        return username
        
    def hash_password(self, password):
        # Hash a password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')

