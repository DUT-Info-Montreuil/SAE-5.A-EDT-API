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

    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Role.sql_row_to_dictionary(row)
        
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        role = Role(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('personal_id', data_if_not_found['personal_id'])
        )

        return role
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats role data in JSON """
        return {
            'id': row[0],              # L'ID du rôle
            'name': row[1],            # Le nom du rôle
            'description': row[2],     # La description du rôle
            'personal_id': row[3]      # L'ID du personnel associé au rôle
        }