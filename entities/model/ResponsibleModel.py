class ResponsibleModel:
    def __init__(self, id, personal_id, teaching_id, personal_last_name, personal_first_name, teaching_title):
        self.id = id
        self.personal_id = personal_id
        self.teaching_id = teaching_id

        # personal
        self.personal_last_name = personal_last_name
        self.personal_first_name = personal_first_name
        
        # teaching
        self.teaching_title = teaching_title
        
    def __str__(self):
        return "Responsible id: %s" % self.id

    def jsonify(self):
        return {
            "id": self.id,
            "personal_id": self.personal_id,
            "teaching_id": self.teaching_id,
            "personal_last_name": self.personal_last_name,
            "personal_first_name": self.personal_first_name,
            "teaching_title": self.teaching_title
        }
