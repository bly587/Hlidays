from member import member

class family:
    #constructor
    def __init__(self):
        self.family = []

    #get list
    def get_family(self):
        return self.family

    #add to family
    def add_to_family(self, person):
        self.family.append(person)

    #print all
    def print_family(self):
        for value in self.family:
            print(value.get_name())
