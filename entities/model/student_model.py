class StudentModel:
    def __init__(self, student_number, last_name, first_name, mail, phone_number, department_id, group_id, subgroup_id,subgroup_name, group_type, group_promotion, department_name, department_degree_type):
        self.student_number = student_number
        self.last_name = last_name
        self.first_name = first_name
        self.mail = mail
        self.phone_number = phone_number
        self.department_id = department_id
        self.group_id = group_id
        self.subgroup_id = subgroup_id
        
        # subgroup / group / departement
        self.subgroup_name = subgroup_name
        self.group_type = group_type
        self.group_promotion = group_promotion
        self.department_name = department_name
        self.department_degree_type = department_degree_type
        
    def __str__(self):
        return "Student student_number : %s" % self.student_number
    
    def jsonify(self):
        return {
            "student_number" : self.student_number,
            "last_name" : self.last_name,
            "first_name" : self.first_name,
            "mail" : self.mail,
            "phone_number" : self.phone_number,
            "department_id" : self.department_id,
            "group_id" : self.group_id,
            "subgroup_id" : self.subgroup_id,
            "subgroup_name" : self.subgroup_name,
            "group_type" : self.group_type,
            "group_promotion" : self.group_promotion,
            "department_name" : self.department_name,
            "department_degree_type" : self.department_degree_type
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        student_instance = StudentModel(
            data.get('student_number', data_if_not_found['student_number']),
            data.get('last_name', data_if_not_found['last_name']),
            data.get('first_name', data_if_not_found['first_name']),
            data.get('mail', data_if_not_found['mail']),
            data.get('phone_number', data_if_not_found['phone_number']),
            data.get('department_id', data_if_not_found['department_id']),
            data.get('group_id', data_if_not_found['group_id']),
            data.get('subgroup_id', data_if_not_found['subgroup_id']),
            data.get('subgroup_name', data_if_not_found['subgroup_name']),
            data.get('group_type', data_if_not_found['group_type']),
            data.get('group_promotion', data_if_not_found['group_promotion']),
            data.get('department_name', data_if_not_found['department_name']),
            data.get('department_degree_type', data_if_not_found['department_degree_type'])
        )

        return student_instance