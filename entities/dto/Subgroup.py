class Subgroup:
    def __init__(self, id, name, group_id):
        self.id = id
        self.name = name
        self.group_id = group_id

    def __str__(self):
        return "Subgroup id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "group_id": self.group_id
        }
    
    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Subgroup.sql_row_to_dictionary(row)
        
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        subgroup = Subgroup(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('group_id', data_if_not_found['group_id'])
        )

        return subgroup
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats subgroup data in JSON"""
        return {
            'id': row[0],              # L'ID du sous-groupe
            'name': row[1],            # Le nom du sous-groupe
            'group_id': row[2]         # L'ID du groupe associé au sous-groupe
        }
