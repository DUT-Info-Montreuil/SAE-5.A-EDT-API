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
        
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        course = Course(
            data.get('id', data_if_not_found['id']),
            data.get('description', data_if_not_found['description']),
            data.get('startTime', data_if_not_found['startTime']),
            data.get('duree', data_if_not_found['duree']),
            data.get('course_type', data_if_not_found['course_type']),
            data.get('personal_id', data_if_not_found['personal_id']),
            data.get('rooms_id', data_if_not_found['rooms_id']),
            data.get('teaching_id', data_if_not_found['teaching_id'])
        )

        return course
