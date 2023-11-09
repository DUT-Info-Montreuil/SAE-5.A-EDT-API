class Group:
    def __init__(self, id, promotion, type, department_id):
        self.id = id
        self.promotion = promotion
        self.type = type
        self.department_id = department_id

    def __str__(self):
        return "Group id: %s, promotion: %s, type: %s" % (self.id, self.promotion, self.type)

    def jsonify(self):
        return {
            "id": self.id,
            "promotion": self.promotion,
            "type": self.type,
            "department_id": self.department_id
        }
