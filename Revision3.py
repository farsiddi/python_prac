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
# print(things["Watch"][1])

student_attendance = {
    "Farhan": 89,
    "Adams": 72,
    "Karan": 88,
    "Rohan": 99
}
# for student in student_attendance:
#     print(f"{student} and attendance = {student_attendance[student]}")
# for student, attendance in student_attendance.items():
#     print(f"{student} and attendance = {attendance}")

x, y = 3, 4
# print(x, y)
tuple1 = 1, 8
x, y = tuple1
# print(x, y)

people = [("Farhan", 21, "Developer"), ("Rohan", 23, "Tester"), ("Sanchay", 22, "Evaluator")]
# for name, age, profession in people:
#     print(f"Name : {name} , Age : {age} , Profession : {profession}")

person1 = ("Farhan", 21, "Developer")
name, _, profession = person1
# print(name, profession)
#
head, head1, *tail = [1, 2, 3, 4, 5, 6, 7]
# print(head, tail, head1)  # head n head1 - int and tail - list
# print(type(tail))


users = [
    (0, "Bob", "bob123"),
    (1, "Adam", "adam123"),
    (2, "Farhan", "far123"),
    (3, "Sam", "sam123")
]
username_mapping = {user[1]: user for user in users}
print(username_mapping["Bob"])

# Getting user information
username_input = input("Enter your username")
password_input = input("Enter your password")
_, username, password = username_mapping[username_input, password_input]
# if password_input == password:
#     print("your details are correct")
# else:
#     print("Your details are incorrect")
print()