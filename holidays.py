from family import family
from member import member
import datetime

#serialize list to file
def serialize(fam_list):
    #write out to file
    f = open("family_members.txt", "w")
    for value in fam_list:
        f.write(value.write_format())
    f.close()

def unserialize():
    #open and read the file after the appending:
    f = open("family_members.txt", "r")
    print(f.read())
    for value in f:
        #read each line as member
        stuff = []
        stuff = value.split(" ")
        print(stuff)

#Get date
def get_date():
    #reformat date to month-day-year
    date = str(datetime.datetime.now())
    #9 is last value
    month = date[5] + date[6]
    day = date[8] + date[9]
    year = date[:4]
    date = month + "/" + day + "/" + year
    return date

def check_birthdate(person, date):
    #person is object member
    #get member's bday
    bday = person.get_birthdate()
    #reformat to only contain month and day
    bday = bday[:5]
    date = date[:5]
    #compare dates and see if they are the same
    if bday == date:
        print("Happy Birthday!")
    else:
        print("Who cares")

date = get_date()
#print(date)
#Read in list of family members
#check if it's any of their bdays
#check if it's a holiday
#Use priority list to let me know I need personalized texts/ calls
#Generate generic texts for other members

unserialize()
test1 = member("Titan Mitchell", 20, '02/21/2000', "808-206-1617")
f = family()
f.add_to_family(test1)
f.print_family()
serialize(f.get_family())
