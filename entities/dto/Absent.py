class Absent:
    def __init__(self, id, justified, student_number, course_id):
        self.id = id
        self.justified = justified
        self.student_number = student_number
        self.course_id = course_id

    def __str__(self):
        return "Absent id: %s, justified: %s" % (self.id, self.justified)

    def jsonify(self):
        return {
            "id": self.id,
            "justified": self.justified,
            "student_number": self.student_number,
            "course_id": self.course_id
        }
