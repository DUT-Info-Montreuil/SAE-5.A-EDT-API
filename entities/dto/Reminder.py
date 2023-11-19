class Reminder:
    def __init__(self, id, name, description, course_id):
        self.id = id
        self.name = name
        self.description = description
        self.course_id = course_id

    def __str__(self):
        return "Reminder id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "course_id": self.course_id
        }

    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Reminder.sql_row_to_dictionary(row)

        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        reminder = Reminder(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('course_id', data_if_not_found['course_id'])
        )

        return reminder
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats reminder data in JSON """
        return {
            'id': row[0],   # L'ID du cours
            'name': row[1],     # Nom du rappel
            'description': row[2],     # Description du rappel
            'course_id': row[3]     # L'ID du cours
        }