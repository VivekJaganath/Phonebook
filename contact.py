class Contact:

    def __init__(self):
        self._name = None
        self._number = None
        self._address = None
        self._email = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def get_contact(self):
        return {'name': self.name,
                'number': self.number,
                'email': self.email,
                'address': self.address
                }