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
