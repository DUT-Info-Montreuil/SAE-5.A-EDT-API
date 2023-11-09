class ReminderModel:
    def __init__(self, id, name, description, course_id, course_startTime, course_duree, course_course_type):
        self.id = id
        self.name = name
        self.description = description
        self.course_id = course_id
        
        # course
        self.course_startTime = course_startTime
        self.course_duree = course_duree
        self.course_course_type = course_course_type

    def __str__(self):
        return "Reminder id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "course_id": self.course_id,
            "course_startTime": self.course_startTime,
            "course_duree": self.course_duree,
            "course_course_type": self.course_course_type
        }
