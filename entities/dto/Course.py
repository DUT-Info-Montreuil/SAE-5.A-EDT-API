class Course:
    def __init__(self, id, description, startTime, duree, course_type, personal_id, rooms_id, teaching_id):
        self.id = id
        self.description = description
        self.startTime = startTime
        self.duree = duree
        self.course_type = course_type
        self.personal_id = personal_id
        self.rooms_id = rooms_id
        self.teaching_id = teaching_id

    def __str__(self):
        return "Course id: %s, description: %s" % (self.id, self.description)

    def jsonify(self):
        return {
            "id": self.id,
            "description": self.description,
            "startTime": str(self.startTime),
            "duree": str(self.duree),
            "course_type": self.course_type,
            "personal_id": self.personal_id,
            "rooms_id": self.rooms_id,
            "teaching_id": self.teaching_id
        }
