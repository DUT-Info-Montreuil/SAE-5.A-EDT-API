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
