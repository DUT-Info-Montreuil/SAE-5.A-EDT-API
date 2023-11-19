class Room:
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
    def objectify(row, data_if_not_found=None):
        data = Room.sql_row_to_dictionary(row)
        
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        room = Room(
            data.get('id', data_if_not_found['id']),
            data.get('code', data_if_not_found['code']),
            data.get('capacity', data_if_not_found['capacity']),
            data.get('has_computer', data_if_not_found['has_computer']),
            data.get('has_projector', data_if_not_found['has_projector'])
        )

        return room
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats room data in JSON """
        return {
            'id': row[0],              # L'ID de la salle
            'code': row[1],            # Le code de la salle
            'capacity': row[2],        # La capacité de la salle
            'has_computer': row[3],    # Indique si la salle a un ordinateur (true ou false)
            'has_projector': row[4]    # Indique si la salle a un projecteur (true ou false)
        }