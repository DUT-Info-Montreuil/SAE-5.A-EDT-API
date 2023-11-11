class DepartmentModel:
    def __init__(self, id, name, description, degree_type, personal_id, personal_last_name, personal_first_name):
        self.id = id
        self.name = name
        self.description = description
        self.degree_type = degree_type
        self.personal_id = personal_id
        
        # departement_responsable 
        self.personal_last_name = personal_last_name
        self.personal_first_name = personal_first_name
        
    def __str__(self):
        return "Department id : %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "degree_type": self.degree_type,
            "personal_id": self.personal_id,
            "personal_last_name": self.personal_last_name,
            "personal_first_name": self.personal_first_name,
        }
