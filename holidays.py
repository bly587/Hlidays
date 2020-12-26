from family import family
from member import member
import datetime
import json
import os
#serialize list to file
def serialize(fam_list):
    #print(fam_list)
    #write out to file
    #f = open("family_members.txt", "w")
    with open('family_members.json', 'w') as json_file:
        # json.dump(fam_list, myobject.__dict__)
        for person in fam_list:
            fam_list[person] = fam_list.get(person).write_format()
            #print(fam_list.get(person).write_format())
            #print(person.write_format())
        json.dump(fam_list, json_file)
    # for value in fam_list:
    #     f.write(value)
    json_file.close()

def unserialize():
    #open and read the file after the appending:
    f = open("family_members.json", "r")
    #print(f.read())
    # for value in f:
    #     #read each line as member
    #     stuff = []
    #     stuff = value.split(" ")
    #     print(stuff)
    #if json file is empty then return empty dictionary
    if os.stat("family_members.json").st_size == 0:
        return {}
    else:
        data = json.loads(f.read())
    #now with the dictionary we need to change values to member objects
    #close file
    f.close()
    print(data)
    #return data because it will be our new family object
    return data

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



date = get_date()
#print(date)
#Read in list of family members
#check if it's any of their bdays
#check if it's a holiday
#Use priority list to let me know I need personalized texts/ calls
#Generate generic texts for other members

f = family()
dict = unserialize()
f.set_family(dict)
#print family for test
#print(f.get_family())
test1 = member("Titan Mitchell", 20, '02/21/2000', "808-206-1617", "important")
test2 = member("Jack Mitchell", 20, '12/24/2000', "808-206-1617", "generic")
# f = family()
f.add_to_family(test1)
f.add_to_family(test2)
# f.print_family()
# f.check_birthdate(date)
serialize(f.get_family())
