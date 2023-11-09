class Teaching:
    def __init__(self, id, title, hour_number, semestre, sequence, description, teaching_type, specialization_id):
        self.id = id
        self.title = title
        self.hour_number = hour_number
        self.semestre = semestre
        self.sequence = sequence
        self.description = description
        self.teaching_type = teaching_type
        self.specialization_id = specialization_id

    def __str__(self):
        return "Teaching id: %s, title: %s" % (self.id, self.title)

    def jsonify(self):
        return {
            "id": self.id,
            "title": self.title,
            "hour_number": self.hour_number,
            "semestre": self.semestre,
            "sequence": self.sequence,
            "description": self.description,
            "teaching_type": self.teaching_type,
            "specialization_id": self.specialization_id
        }
