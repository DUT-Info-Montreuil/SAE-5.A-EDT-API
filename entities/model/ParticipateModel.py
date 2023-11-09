class ParticipateModel:
    def __init__(self, id, course_id, subgroup_id, course_description, course_startTime, course_duree, course_type, subgroup_name, group_type, group_promotion, department_name):
        self.id = id
        self.course_id = course_id
        self.subgroup_id = subgroup_id
        
        # course
        self.course_description = course_description
        self.course_startTime = course_startTime
        self.course_duree = course_duree
        self.course_type = course_type
        
        # subgroup / group / departement
        self.subgroup_name = subgroup_name
        self.group_type = group_type
        self.group_promotion = group_promotion
        self.department_name = department_name
        

    def __str__(self):
        return "Participate id: %s" % self.id

    def jsonify(self):
        return {
            "id": self.id,
            "course_id": self.course_id,
            "course_description": self.course_description,
            "course_startTime": self.course_startTime,
            "course_duree": self.course_duree,
            "course_type": self.course_type,
            "subgroup_name": self.subgroup_name,
            "group_type": self.group_type,
            "group_promotion": self.group_promotion,
            "department_name": self.department_name
        }
