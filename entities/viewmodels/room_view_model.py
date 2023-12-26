class RoomViewModel:
    def __init__(self, id, code, capacity, has_computer=True, has_projector=True):
        self.id = id
        self.code = code
        self.capacity = capacity
        self.has_computer = has_computer
        self.has_projector = has_projector

    def __str__(self):
        return "Room id: %s, code: %s" % (self.id, self.code)

    def jsonify(self):
        return {
            "id": self.id,
            "code": self.code,
            "capacity": self.capacity,
            "has_computer": self.has_computer,
            "has_projector": self.has_projector
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        room_instance = RoomViewModel(
            data.get('id', data_if_not_found['id']),
            data.get('code', data_if_not_found['code']),
            data.get('capacity', data_if_not_found['capacity']),
            data.get('has_computer', data_if_not_found['has_computer']),
            data.get('has_projector', data_if_not_found['has_projector'])
        )

        return room_instance