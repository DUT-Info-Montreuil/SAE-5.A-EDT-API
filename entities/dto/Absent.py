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
        
    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Absent.sql_row_to_dictionary(row)
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        absent = Absent(
            data.get('id', data_if_not_found['id']),
            data.get('justified', data_if_not_found['justified']),
            data.get('student_number', data_if_not_found['student_number']),
            data.get('course_id', data_if_not_found['course_id'])
        )

        return absent
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats absent data in JSON """
        return {
            'id': row[0],              # L'ID de l'absent
            'justified': row[1],     # La justification (t ou f)
            'student_number': row[2],       # Le numero etudiant de l'absent
            'course_id': row[3],           # L'ID du cours
        }
