# Conditionals

# days = input("What day is today ?").capitalize()
# print(days == "Monday")
# if days == "Monday":
#     print(True)
# elif days == "Tuesday":
#     print("Go ahead")
# else:
#     print(False)

day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# if "Thursday" in day_name:
#     print("Contains")
#
# if "May" in day_name:
#     print("Month contain")
# else:
#     print("Doesnt contains")

magic_number = 6
# user_number = int(input("Enter the Number: "))
marks = [11, 44, 84, 22, 64, 75]
total = 0
# total = sum(marks)
count = 0
for i in marks:
    total = total + i
    count += 1
# print(f"Average = {total / count}")

new_list = [x + 10 for x in marks]
# print(new_list)

friends = ["Aditya", "Farhan", "Alok", "Sanchay", "Abhishek", "Ajay"]
new_name = []
for name in friends:
    if name[0] == "A":
        # if name.startswith('A'):
        # print(name)
        new_name.append(name)
# print(new_name)

# new_name1 = [name.startswith("A") for name in friends]
new_name1 = [name for name in friends if name.startswith("A")]
# print(new_name1)


things = {
    "Phone": ["Nokia", "Apple", "Samsung"],
    "Car": ["Ferrari", "Toyota", "Nissan"],
    "Watch": ["Patek", "Rado", "Casio"]
}
print(things["Watch"][1])

student_attendance = {
    "Farhan": 89,
    "Adams": 72,
    "Karan": 88,
    "Rohan": 99
}
# for student in student_attendance:
#     print(f"{student} and attendance = {student_attendance[student]}")
for student,attendance in student_attendance.items():
    print(f"{student} and attendance = {attendance}")

