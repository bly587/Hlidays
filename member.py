class member:
    #consturctor
    def __init__(self, name, age = 0, birthdate = " ", phone = " "):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.phone = phone

    #functions
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_birthdate(self):
        return self.birthdate

    def get_phone(self):
        return self.phone

    #setters
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
    def set_phone(self, phone):
        self.phone = phone

    #format informaiton to be serialized
    def write_format(self):
        #make everything strings
        name = self.name
        age = str(self.age)
        birthdate = self.birthdate
        phone = str(self.phone)
        #seperate everything with a space
        sentence = name + " " + age + " " + birthdate + " " + phone
        return sentence
