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
    
    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Specialization.sql_row_to_dictionary(row)
        
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        specialization = Specialization(
            data.get('id', data_if_not_found['id']),
            data.get('code', data_if_not_found['code']),
            data.get('name', data_if_not_found['name']),
            data.get('department_id', data_if_not_found['department_id'])
        )

        return specialization
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats specialization data in JSON """
        return {
            'id': row[0],               # L'ID de la spécialisation
            'code': row[1],             # Le code de la spécialisation
            'name': row[2],             # Le nom de la spécialisation
            'department_id': row[3]     # L'ID du département associé à la spécialisation
        }
