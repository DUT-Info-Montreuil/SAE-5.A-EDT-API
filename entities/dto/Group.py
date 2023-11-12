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
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        group = Group(
            data.get('id', data_if_not_found['id']),
            data.get('promotion', data_if_not_found['promotion']),
            data.get('type', data_if_not_found['type']),
            data.get('department_id', data_if_not_found['department_id'])
        )

        return group
