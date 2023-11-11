class RoleModel:
    def __init__(self, id, name, description, personal_id, personal_last_name, personal_first_name):
        self.id = id
        self.name = name
        self.description = description
        self.personal_id = personal_id

        # personal
        self.personal_last_name = personal_last_name
        self.personal_first_name = personal_first_name
        
    def __str__(self):
        return "Role id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "personal_id": self.personal_id,
            "personal_last_name": self.personal_last_name,
            "personal_first_name": self.personal_first_name
        }
