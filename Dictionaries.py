# Append is used with List only not with Dictionary
# For loops in dictionary works in iterating keys
prg_dic = {"name": "Farhan Siddiqui",
           "loca": "Pune",
           "Phone_no": "123131"
           }
print(prg_dic["Phone_no"])

# Adding
prg_dic["dept"] = "Cloud"
print(prg_dic)

# Editing
prg_dic["name"] = "Rahul"
print(prg_dic)
# If not in the dictionary it will create a one key value
prg_dic["floor"] = "5th"

print(prg_dic)
print("hello")

for key in prg_dic:
    print(key)
    print(prg_dic[key])

    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    # TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    # TODO-2: Covert scores into grades.
    for student in student_scores:
        score = student_scores[student]
        if score > 90:
            student_grades[student] = "Outstanding"
        elif score > 80:
            student_grades[student] = "Exceeds Expectations"
        elif score > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)