class Subgroup:
    def __init__(self, id, name, group_id):
        self.id = id
        self.name = name
        self.group_id = group_id

    def __str__(self):
        return "Subgroup id: %s, name: %s" % (self.id, self.name)

    def jsonify(self):
        return {
            "id": self.id,
            "name": self.name,
            "group_id": self.group_id
        }
