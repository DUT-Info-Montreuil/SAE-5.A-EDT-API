class RoleViewModel:
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
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        role_instance = RoleViewModel(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('personal_id', data_if_not_found['personal_id']),
            data.get('personal_last_name', data_if_not_found['personal_last_name']),
            data.get('personal_first_name', data_if_not_found['personal_first_name'])
        )

        return role_instance
