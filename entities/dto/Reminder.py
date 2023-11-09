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
