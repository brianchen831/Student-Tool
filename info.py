import csv
from csv import reader, writer 

with open ('college-data.csv', 'r', encoding='utf-8') as file:
    csv_file = list(csv.reader(file))

university = ""
search = input("Enter the name of the Texas university you're interested in: ")
search_results = []
for line in csv_file:
    university_names = line[1]

    university_names = university_names.split("\n")
    for university in university_names: 
        if search in university:
            search_results.append(university)

num_diff = 1
num_same = -1
college = ""
if len(search_results) > 1:
    print("Multiple results found for \"" + search + "\"")
    print("[", 1, "]", search_results[0])
    for i in range(len(search_results) - 1):
        if search_results[i] != search_results[i + 1]:
            print("[", num_diff+1, "]", search_results[i+1])
            num_diff += 1
        else:
            num_same += 1
    num_university = int(input("Select 1-" + str(num_diff) + ": "))
    college = search_results[num_university * 9 - 2]
    print(college)

ethnicities = ["Total", "White", "African American", "Hispanic", "Asian"]
genders = ["Total", "Male", "Female", "Other"]

for i in range(len(ethnicities)):
    print("[", i+1, "]", ethnicities[i])
num_ethnicities = int(input("Would you like to search based on ethnicity? Select 1-5. (Ex; White = 2) ")) - 1

info = ["","","","","","","","",""]
if num_ethnicities == 0:
    for i in range(len(genders)):
        print("[", i+1, "]", genders[i])
    num_genders = int(input("Would you like to search based on gender? Select 1-4. (Ex; Male = 2) ")) - 1
    for line in csv_file:
        if "Fice Code" in line:
            for i in range(9):
                info[i] += line[i]
        if college in line:
            if genders[num_genders] in line[2]:
                for i in range(9):
                    info[i] += " - " + line[i]
    for item in info:
        print(item)
else:
    for line in csv_file:
        if "Fice Code" in line:
            for i in range(9):
                info[i] += line[i]
        if college in line:
            if ethnicities[num_ethnicities] in line[2]:
                for i in range(9):
                    info[i] += " - " + line[i]
    for item in info:
        print(item)