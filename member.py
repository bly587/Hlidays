class member:
    #type should have 3 options
    #generic, important, personal
    #generic means simple automated message
    #important means complex automated message
    #personal means should be sent a personal message
    #consturctor
    def __init__(self, name, age = 0, birthdate = " ", phone = " ", ptype = "generic"):
        self.name = name
        self.age = age
        self.birthdate = birthdate
        self.phone = phone
        self.ptype = ptype
        self.info = [name, age, birthdate, phone, ptype]

    #functions

    def get_name(self):
        return self.name

    def get_age(self):
        return self.get_age

    def get_birthdate(self):
        return self.birthdate

    def get_phone(self):
        return self.phone

    def get_type(self):
        return self.ptype

    #setters
    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
    def set_phone(self, phone):
        self.phone = phone
    def set_ptype(self, ptype):
        self.ptype = ptype

    #format informaiton to be serialized
    def write_format(self):
        #make everything strings
        # name = self.name
        # age = str(self.age)
        # birthdate = self.birthdate
        # phone = str(self.phone)
        # ptype = self.ptype
        #Then add values to a list
        info = [self.name, self.age, self.birthdate, self.phone, self.ptype]
        # sentence = name + " " + age + " " + birthdate + " " + phone + " " + ptype
        # return sentence
        return info
