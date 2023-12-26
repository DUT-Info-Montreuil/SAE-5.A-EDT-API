class TeachingViewModel:
    def __init__(self, id, title, hour_number, semestre, sequence, description, teaching_type, specialization_id, specialization_code, specialization_name, specialization_department_id, specialization_department_degree_type):
        self.id = id
        self.title = title
        self.hour_number = hour_number
        self.semestre = semestre
        self.sequence = sequence
        self.description = description
        self.teaching_type = teaching_type
        self.specialization_id = specialization_id

        # specialization
        self.specialization_code = specialization_code
        self.specialization_name = specialization_name
        self.specialization_department_id = specialization_department_id
        self.specialization_department_degree_type = specialization_department_degree_type

    def __str__(self):
        return "Teaching id: %s, title: %s" % (self.id, self.title)

    def jsonify(self):
        return {
            "id": self.id,
            "title": self.title,
            "hour_number": self.hour_number,
            "semestre": self.semestre,
            "sequence": self.sequence,
            "description": self.description,
            "teaching_type": self.teaching_type,
            "specialization_id": self.specialization_id,
            "specialization_code": self.specialization_code,
            "specialization_name": self.specialization_name,
            "specialization_department_id": self.specialization_department_id,
            "specialization_department_degree_type": self.specialization_department_degree_type
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        teaching_instance = TeachingViewModel(
            data.get('id', data_if_not_found['id']),
            data.get('title', data_if_not_found['title']),
            data.get('hour_number', data_if_not_found['hour_number']),
            data.get('semestre', data_if_not_found['semestre']),
            data.get('sequence', data_if_not_found['sequence']),
            data.get('description', data_if_not_found['description']),
            data.get('teaching_type', data_if_not_found['teaching_type']),
            data.get('specialization_id', data_if_not_found['specialization_id']),
            data.get('specialization_code', data_if_not_found['specialization_code']),
            data.get('specialization_name', data_if_not_found['specialization_name']),
            data.get('specialization_department_id', data_if_not_found['specialization_department_id']),
            data.get('specialization_department_degree_type', data_if_not_found['specialization_department_degree_type'])
        )

        return teaching_instance