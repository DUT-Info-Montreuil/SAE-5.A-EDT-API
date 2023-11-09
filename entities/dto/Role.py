class Role:
    def __init__(self, id, name, description, personal_id):
        self.id = id
        self.name = name
        self.description = description
        self.personal_id = personal_id

    def __str__(self):
        return "Role id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "personal_id": self.personal_id
        }
