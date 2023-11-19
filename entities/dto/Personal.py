class Personal:
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
    def objectify(row, data_if_not_found=None):
        data = Personal.sql_row_to_dictionary(row)

        if data_if_not_found is None:
            data_if_not_found = {key: '' for key in data}

        personal = Personal(
            data.get('id', data_if_not_found['id']),
            data.get('last_name', data_if_not_found['last_name']),
            data.get('first_name', data_if_not_found['first_name']),
            data.get('mail', data_if_not_found['mail']),
            data.get('phone_number', data_if_not_found['phone_number'])
        )

        return personal
    
    @staticmethod
    def sql_row_to_dictionary(row):
        """ Formats personal data in JSON """
        return {
            'id': row[0],              # L'ID du personnel
            'last_name': row[1],       # Le nom de famille du personnel
            'first_name': row[2],      # Le prénom du personnel
            'mail': row[3],            # L'adresse e-mail du personnel
            'phone_number': row[4]     # Le numéro de téléphone du personnel
        }
