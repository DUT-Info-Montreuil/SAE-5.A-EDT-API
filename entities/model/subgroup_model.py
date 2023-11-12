class SubgroupModel:
    def __init__(self, id, name, group_id, group_promotion, group_type, department_name, department_description, department_degree_type):
        self.id = id
        self.name = name
        self.group_id = group_id
        
        # group
        self.group_promotion = group_promotion
        self.group_type = group_type
        
        # department
        self.department_name = department_name
        self.department_description = department_description
        self.department_degree_type = department_degree_type

    def __str__(self):
        return "Subgroup id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "group_id": self.group_id,
            "group_promotion": self.group_promotion,
            "group_type": self.group_type,
            "department_name": self.department_name,
            "department_description": self.department_description,
            "department_degree_type": self.department_degree_type
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        subgroup_instance = SubgroupModel(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('group_id', data_if_not_found['group_id']),
            data.get('group_promotion', data_if_not_found['group_promotion']),
            data.get('group_type', data_if_not_found['group_type']),
            data.get('department_name', data_if_not_found['department_name']),
            data.get('department_description', data_if_not_found['department_description']),
            data.get('department_degree_type', data_if_not_found['department_degree_type'])
        )

        return subgroup_instance