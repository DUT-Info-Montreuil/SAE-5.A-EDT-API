class Specialization:
    def __init__(self, id, code, name, department_id):
        self.id = id
        self.code = code
        self.name = name
        self.department_id = department_id

    def __str__(self):
        return "Specialization id: %s, code: %s" % (self.id, self.code)

    def jsonify(self):
        return {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "department_id": self.department_id
        }
