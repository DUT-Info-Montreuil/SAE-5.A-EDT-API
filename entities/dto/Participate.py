class Participate:
    def __init__(self, id, course_id, subgroup_id):
        self.id = id
        self.course_id = course_id
        self.subgroup_id = subgroup_id

    def __str__(self):
        return "Participate id: %s" % self.id

    def jsonify(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "subgroup_id": self.subgroup_id
        }

    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        participate = Participate(
            data.get('id', data_if_not_found['id']),
            data.get('course_id', data_if_not_found['course_id']),
            data.get('subgroup_id', data_if_not_found['subgroup_id'])
        )

        return participate