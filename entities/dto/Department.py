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
        
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        department = Department(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('degree_type', data_if_not_found['degree_type']),
            data.get('personal_id', data_if_not_found['personal_id'])
        )

        return department
