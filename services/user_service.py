from services.sql_alchemy_service import db
from entities.models.models import User

class UserService:
    def get_all_users(self):
        users = User.query.all()
        user_list = []

        for user in users:
            user_data = user.get_json()
            user_list.append(user_data)

        return user_list
    
    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)

        if user:
            user_data = user.get_json()
            return user_data
        else:
            return None
    
    def find_user(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        users = User.query.filter_by(**conditions)

        user_list = []

        for user in users:
            user_list.append(user.get_json())

        return user_list
    
    def delete_user(self, user_id):
        user = User.query.get(user_id)

        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False
    
    def update_user(self, user_id, new_data):
        user = User.query.get(user_id)

        if user:
            for key, value in new_data.items():
                setattr(user, key, value)

            db.session.commit()
            return True
        else:
            return False

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