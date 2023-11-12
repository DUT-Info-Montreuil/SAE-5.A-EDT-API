class SpecializationModel:
    def __init__(self, id, code, name, department_id, department_name, department_description, department_degree_type):
        self.id = id
        self.code = code
        self.name = name
        self.department_id = department_id
        
        # department
        self.department_name = department_name
        self.department_description = department_description
        self.department_degree_type = department_degree_type

    def __str__(self):
        return "Specialization id: %s, code: %s" % (self.id, self.code)

    def jsonify(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "department_id": self.department_id,
            "department_name": self.department_name,
            "department_description": self.department_description,
            "department_degree_type": self.department_degree_type
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        specialization_instance = SpecializationModel(
            data.get('id', data_if_not_found['id']),
            data.get('code', data_if_not_found['code']),
            data.get('name', data_if_not_found['name']),
            data.get('department_id', data_if_not_found['department_id']),
            data.get('department_name', data_if_not_found['department_name']),
            data.get('department_description', data_if_not_found['department_description']),
            data.get('department_degree_type', data_if_not_found['department_degree_type'])
        )

        return specialization_instance
