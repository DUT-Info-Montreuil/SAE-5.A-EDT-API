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
            "last_name" : self.last_name,
            "first_name" : self.first_name,
            "startTime": str(self.startTime),
            "duree": str(self.duree),
            "course_type": self.course_type,
            "teaching_id": self.teaching_id,
            "teaching_title": self.teaching_title
        }
