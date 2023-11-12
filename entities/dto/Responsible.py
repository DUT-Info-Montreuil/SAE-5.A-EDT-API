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

    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        responsible = Responsible(
            data.get('id', data_if_not_found['id']),
            data.get('personal_id', data_if_not_found['personal_id']),
            data.get('teaching_id', data_if_not_found['teaching_id'])
        )

        return responsible