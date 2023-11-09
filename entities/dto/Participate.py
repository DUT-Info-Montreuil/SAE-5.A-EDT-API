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
