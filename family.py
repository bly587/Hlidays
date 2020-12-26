from member import member

class family:
    #constructor
    def __init__(self):
        self.family = {}

    #get list
    def get_family(self):
        return self.family

    #set list
    def set_family(self, fam):
        self.family = fam

    #add to family
    def add_to_family(self, person):
        #dictonary uses name as key and stores member object as value
        self.family[person.get_name()] = person

    #print all
    def print_family(self):
        for value in self.family.keys():
            print(self.family.get(value))

    # def check_birthdate(self, date):
    #     #return list of people who have birthdays today
    #     bday_list = []
    #     #person is object member
    #     for key in self.family.keys():
    #         person = self.family.get(key)
    #         #get member's bday
    #         bday = person.get_birthdate()
    #         #reformat to only contain month and day
    #         bday = bday[:5]
    #         date = date[:5]
    #         #compare dates and see if they are the same
    #         if bday == date:
    #             print("Happy Birthday!: " +person.get_name())
    #         else:
    #             print("Who cares")
