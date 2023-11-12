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
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        responsible_instance = ResponsibleModel(
            data.get('id', data_if_not_found['id']),
            data.get('personal_id', data_if_not_found['personal_id']),
            data.get('teaching_id', data_if_not_found['teaching_id']),
            data.get('personal_last_name', data_if_not_found['personal_last_name']),
            data.get('personal_first_name', data_if_not_found['personal_first_name']),
            data.get('teaching_title', data_if_not_found['teaching_title'])
        )

        return responsible_instance
   