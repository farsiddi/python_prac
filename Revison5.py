# students = {"name": "Rolf", "grades": (56, 87, 98)}


def average(seq):
    return sum(seq) / len(seq)


# print(average(students["grades"]))

class Student:
    # def __init__(self):
    #     self.name = "Farhan"
    #     self.grades = (87, 98, 78, 79)
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Farhan", (87, 98, 78, 79))
student1 = Student("Sanchay", (89, 67, 98, 93))


# print(student.name)
# print(student1.name)
# print(student.grades)
# print(sum(student.grades) / len(student.grades))
# print(Student.average(student))
# print(student.average())
# print(student1.average())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Hello"


bob = Person("Bob", 35)
print(bob)
