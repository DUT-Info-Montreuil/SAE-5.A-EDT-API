class GroupModel:
    def __init__(self, id, promotion, type, department_id, department_name, department_description, department_degree_type):
        self.id = id
        self.promotion = promotion
        self.type = type
        self.department_id = department_id
        
        # department
        self.department_name = department_name
        self.department_description = department_description
        self.department_degree_type = department_degree_type
        
    def __str__(self):
        return "Group id: %s, promotion: %s, type: %s" % (self.id, self.promotion, self.type)

    def jsonify(self):
        return {
            "id": self.id,
            "promotion": self.promotion,
            "type": self.type,
            "department_id": self.department_id,
            "department_name": self.department_name,
            "department_description": self.department_description,
            "department_degree_type": self.department_degree_type
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        group_instance = GroupModel(
            data.get('id', data_if_not_found['id']),
            data.get('promotion', data_if_not_found['promotion']),
            data.get('type', data_if_not_found['type']),
            data.get('department_id', data_if_not_found['department_id']),
            data.get('department_name', data_if_not_found['department_name']),
            data.get('department_description', data_if_not_found['department_description']),
            data.get('department_degree_type', data_if_not_found['department_degree_type'])
        )

        return group_instance