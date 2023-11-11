class RoomModel:
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
