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
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        reminder = Reminder(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('course_id', data_if_not_found['course_id'])
        )

        return reminder