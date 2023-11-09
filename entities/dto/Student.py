class Student:
    def __init__(self, student_number, last_name, first_name, mail, phone_number, department_id, group_id, subgroup_id):
        self.student_number = student_number
        self.last_name = last_name
        self.first_name = first_name
        self.mail = mail
        self.phone_number = phone_number
        self.department_id = department_id
        self.group_id = group_id
        self.subgroup_id = subgroup_id
        
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
            "subgroup_id" : self.subgroup_id
        }