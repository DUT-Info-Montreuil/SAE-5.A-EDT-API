from services.main_basic_service import *
from configuration import connect_pg

"""
Rooms
university.roles(@id, name, description, personal_id)"""
class room_service(Service):
    # === region : Room ===
    def get_all_rooms(self):
        rooms = Room.query.all()
        room_list = []

        for room in rooms:
            room_data = room.get_json()
            room_list.append(room_data)

        return room_list
    
    def get_room_by_id(self, room_id):
        room = Room.query.get(room_id)

        if room:
            room_data = room.get_json()
            return room_data
        else:
            return None
    
    def find_room(self, **kwargs):
        # Construct filter conditions dynamically
        conditions = {key: value for key, value in kwargs.items() if value is not None}
        
        rooms = Room.query.filter_by(**conditions)

        room_list = []

        for room in rooms:
            room_list.append(room.get_json())

        return room_list
    
    def delete_room(self, room_id):
        room = Room.query.get(room_id)

        if room:
            db.session.delete(room)
            db.session.commit()
            return True
        else:
            return False
    
    def update_room(self, room_id, new_data):
        room = Room.query.get(room_id)

        if room:
            for key, value in new_data.items():
                setattr(room, key, value)

            db.session.commit()
            return True
        else:
            return False
    
    def add_room(self, room_data):
        new_room = Room(**room_data)

        try:
            db.session.add(new_room)
            db.session.commit()
            return new_room.get_json()
        except Exception as e:
            # Handle exceptions (e.g., integrity errors) appropriately
            db.session.rollback()
            return None
    # === endregion : Room ===