class PersonalViewModel:
    def __init__(self, id, last_name, first_name, mail, phone_number):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.mail = mail
        self.phone_number = phone_number

    def __str__(self):
        return "Personal id: %s, last_name: %s, first_name: %s" % (self.id, self.last_name, self.first_name)

    def jsonify(self):
        return {
            "id": self.id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "mail": self.mail,
            "phone_number": self.phone_number
        }
    
    @staticmethod
    def objectify(data, data_if_not_found=None):
        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        personal_instance = PersonalViewModel(
            data.get('id', data_if_not_found['id']),
            data.get('last_name', data_if_not_found['last_name']),
            data.get('first_name', data_if_not_found['first_name']),
            data.get('mail', data_if_not_found['mail']),
            data.get('phone_number', data_if_not_found['phone_number'])
        )

        return personal_instance