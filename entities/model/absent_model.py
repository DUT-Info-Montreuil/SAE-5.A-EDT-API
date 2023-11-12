class AbsentModel:
    def __init__(self, id, justified, student_number, course_id, last_name, first_name, startTime, duree, course_type, teaching_id, teaching_title):
        self.id = id
        self.justified = justified
        self.student_number = student_number
        self.course_id = course_id

        # student
        self.last_name = last_name
        self.first_name = first_name

        # course
        self.startTime = startTime
        self.duree = duree
        self.course_type = course_type

        # teaching
        self.teaching_id = teaching_id
        self.teaching_title = teaching_title

    def __str__(self):
        return "Absent id: %s, last_name: %s, first_name: %s, justified: %s" % (self.id, self.last_name, self.first_name, self.justified)

    def jsonify(self):
        return {
            "id": self.id,
            "justified": self.justified,
            "student_number": self.student_number,
            "course_id": self.course_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "startTime": str(self.startTime),
            "duree": str(self.duree),
            "course_type": self.course_type,
            "teaching_id": self.teaching_id,
            "teaching_title": self.teaching_title
        }

    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        absent_instance = AbsentModel(
            data.get('id', data_if_not_found['id']),
            data.get('justified', data_if_not_found['justified']),
            data.get('student_number', data_if_not_found['student_number']),
            data.get('course_id', data_if_not_found['course_id']),
            data.get('last_name', data_if_not_found['last_name']),
            data.get('first_name', data_if_not_found['first_name']),
            data.get('startTime', data_if_not_found['startTime']),
            data.get('duree', data_if_not_found['duree']),
            data.get('course_type', data_if_not_found['course_type']),
            data.get('teaching_id', data_if_not_found['teaching_id']),
            data.get('teaching_title', data_if_not_found['teaching_title'])
        )

        return absent_instance
