class DepartmentModel:
    def __init__(self, id, name, description, degree_type, personal_id, personal_last_name, personal_first_name):
        self.id = id
        self.name = name
        self.description = description
        self.degree_type = degree_type
        self.personal_id = personal_id

        # department_responsable
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

    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        department_instance = DepartmentModel(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('degree_type', data_if_not_found['degree_type']),
            data.get('personal_id', data_if_not_found['personal_id']),
            data.get('personal_last_name', data_if_not_found['personal_last_name']),
            data.get('personal_first_name', data_if_not_found['personal_first_name'])
        )

        return department_instance
