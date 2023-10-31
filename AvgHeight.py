# Input a Python list of student heights
student_heights = [156, 178, 165, 171, 187]
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sum_height = 0
no_of_student = 0
for i in student_heights:
    sum_height += i
    no_of_student += 1
average_height = round(sum_height / no_of_student)
print(f"total height = {sum_height}")
print(f"number of students = {no_of_student}")
print(f"average height = {average_height}")
