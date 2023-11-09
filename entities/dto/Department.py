class Department:
    def __init__(self, id, name, description, degree_type, personal_id):
        self.id = id
        self.name = name
        self.description = description
        self.degree_type = degree_type
        self.personal_id = personal_id

    def __str__(self):
        return "Department id : %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "degree_type": self.degree_type,
            "personal_id": self.personal_id
        }
