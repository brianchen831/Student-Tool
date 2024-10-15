import csv
with open ('college-data.csv', 'r', encoding='utf-8') as file:
    csv_file = list(csv.reader(file))
difficulty = int(input(("How easy is the school to get into? Select 1-32. Ex: 1 would be the easiest: ")))
print("[", 1, "]", "All Applicants")
print("[", 2, "]", "White")
print("[", 3, "]", "African American")
print("[", 4, "]", "Hispanic")
print("[", 5, "]", "Asian")
ethnicities = ["White", "African American", "Hispanic", "Asian"]
num_race = int(input("Would you like all applicants or a specific ethnicity? Select 1-5: "))
if num_race == 1:
    print("[", 1, "]", "All Applicants")
    print("[", 2, "]", "Male")
    print("[", 3, "]", "Female")
    print("[", 4, "]", "Other")
    genders = ["Total", "Male", "Female", "Other"]
    num_gender = int(input("Would you like data of all applicants or a specific gender? Select 1-4: "))
    tupleList = []
    tupleList.append(("", 0))
    for line in csv_file:
        tupleList = sorted(tupleList, key=lambda tup: tup[1])
        if line[5] != "% Accepted of Total Texas Applied" and line[5] != "*" and float(line[5].rstrip("%")) > tupleList[0][1] and genders[num_gender-1] in line:
            if len(tupleList) == difficulty:
                tupleList.pop(0)
            tupleList.append((line[1], float(line[5].rstrip("%"))))
    if str(difficulty)[-1] == "1":
        difficulty_str = str(difficulty) + "st"
        print(genders[num_gender-1], difficulty_str, "hardest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    elif str(difficulty)[-1] == "2":
        difficulty_str = str(difficulty) + "nd"
        print(genders[num_gender-1], difficulty_str, "hardest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    elif str(difficulty)[-1] == "3":
        difficulty_str = str(difficulty) + "rd"
        print(genders[num_gender-2], difficulty_str, "easiest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    else:
        difficulty_str = str(difficulty) + "th"
        print(genders[num_gender-1], difficulty_str, "hardest school is", tupleList[0][0], "-", tupleList[0][1], "%")
else:
    tupleList = []
    tupleList.append(("", 0))
    for line in csv_file:
        tupleList = sorted(tupleList, key=lambda tup: tup[1])
        if line[5] != "% Accepted of Total Texas Applied" and line[5] != "*" and float(line[5].rstrip("%")) > tupleList[0][1] and ethnicities[num_race-2] in line:
            if len(tupleList) == difficulty:
                tupleList.pop(0)
            tupleList.append((line[1], float(line[5].rstrip("%"))))
    if str(difficulty)[-1] == "1":
        difficulty_str = str(difficulty) + "st"
        print(ethnicities[num_race-2], difficulty_str, "easiest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    elif str(difficulty)[-1] == "2":
        difficulty_str = str(difficulty) + "nd"
        print(ethnicities[num_race-2], difficulty_str, "easiest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    elif str(difficulty)[-1] == "3":
        difficulty_str = str(difficulty) + "rd"
        print(ethnicities[num_race-2], difficulty_str, "easiest school is", tupleList[0][0], "-", tupleList[0][1], "%")
    else:
        difficulty_str = str(difficulty) + "th"
        print(ethnicities[num_race-2], difficulty_str, "easiest school is", tupleList[0][0], "-", tupleList[0][1], "%")