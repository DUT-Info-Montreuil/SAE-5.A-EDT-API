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
    
    @staticmethod
    def objectify(row, data_if_not_found=None):
        data = Student.sql_row_to_dictionary(row)
        
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        student = Student(
            data.get('student_number', data_if_not_found['student_number']),
            data.get('last_name', data_if_not_found['last_name']),
            data.get('first_name', data_if_not_found['first_name']),
            data.get('mail', data_if_not_found['mail']),
            data.get('phone_number', data_if_not_found['phone_number']),
            data.get('department_id', data_if_not_found['department_id']),
            data.get('group_id', data_if_not_found['group_id']),
            data.get('subgroup_id', data_if_not_found['subgroup_id'])
        )

        return student
    
    @staticmethod
    def sql_row_to_dictionary(row):
        return {
            'student_number': row[0],    # Numero étudiant
            'last_name': row[1],         # Le nom de famille de l'étudiant
            'first_name': row[2],        # Le prénom de l'étudiant
            'mail': row[3],              # L'adresse e-mail de l'étudiant
            'phone_number': row[4],      # Le numéro de téléphone de l'étudiant
            'department_id': row[5],     # L'ID du département auquel l'étudiant est affilié
            'group_id': row[6],          # L'ID du groupe auquel l'étudiant appartient
            'subgroup_id': row[7]        # L'ID du sous-groupe auquel l'étudiant est associé
        }