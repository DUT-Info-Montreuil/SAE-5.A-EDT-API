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
    def objectify(row, data_if_not_found=None):
        data = Group.sql_row_to_dictionary(row)

        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        group = Group(
            data.get('id', data_if_not_found['id']),
            data.get('promotion', data_if_not_found['promotion']),
            data.get('type', data_if_not_found['type']),
            data.get('department_id', data_if_not_found['department_id'])
        )

        return group
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats group data in JSON"""
        return {
            'id': row[0],              # L'ID du groupe
            'promotion': row[1],       # La promotion du groupe
            'type': row[2],            # Le type du groupe
            'department_id': row[3]    # L'ID du département associé au groupe
        }