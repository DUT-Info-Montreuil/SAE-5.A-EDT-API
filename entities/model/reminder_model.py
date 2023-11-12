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
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        reminder_instance = ReminderModel(
            data.get('id', data_if_not_found['id']),
            data.get('name', data_if_not_found['name']),
            data.get('description', data_if_not_found['description']),
            data.get('course_id', data_if_not_found['course_id']),
            data.get('course_startTime', data_if_not_found['course_startTime']),
            data.get('course_duree', data_if_not_found['course_duree']),
            data.get('course_course_type', data_if_not_found['course_course_type'])
        )

        return reminder_instance