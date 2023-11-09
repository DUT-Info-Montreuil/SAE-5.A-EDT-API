class PersonalModel:
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
