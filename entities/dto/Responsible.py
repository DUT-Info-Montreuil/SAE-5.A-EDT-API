class Responsible:
    def __init__(self, id, personal_id, teaching_id):
        self.id = id
        self.personal_id = personal_id
        self.teaching_id = teaching_id

    def __str__(self):
        return "Responsible id: %s" % self.id

    def jsonify(self):
        return {
            "id": self.id,
            "personal_id": self.personal_id,
            "teaching_id": self.teaching_id
        }
