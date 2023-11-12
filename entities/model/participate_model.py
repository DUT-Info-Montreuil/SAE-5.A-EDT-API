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
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        participate_instance = ParticipateModel(
            data.get('id', data_if_not_found['id']),
            data.get('course_id', data_if_not_found['course_id']),
            data.get('subgroup_id', data_if_not_found['subgroup_id']),
            data.get('course_description', data_if_not_found['course_description']),
            data.get('course_startTime', data_if_not_found['course_startTime']),
            data.get('course_duree', data_if_not_found['course_duree']),
            data.get('course_type', data_if_not_found['course_type']),
            data.get('subgroup_name', data_if_not_found['subgroup_name']),
            data.get('group_type', data_if_not_found['group_type']),
            data.get('group_promotion', data_if_not_found['group_promotion']),
            data.get('department_name', data_if_not_found['department_name'])
        )

        return participate_instance