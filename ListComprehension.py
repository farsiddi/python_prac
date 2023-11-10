numbers = [1, 2, 3, 4]
# new_list = []
# for num in numbers:
#     add_1 = num + 1
#     new_list.append(add_1)
#
# print(new_list)

# using List comprehension
# new_list = [expression for num in numbers]
new_list = [num + 1 for num in numbers]  # Expression => num + 1
# print(new_list)
name = "farhan"
new_name = [letter for letter in name]
# print(new_name)
new_range = [num * 2 for num in range(1, 5)]
print(new_range)

# Conditional list Comprehension
# new_list = [expression for item in old_list if condition]   => only if the condition is true
names = ["Alex", "Beth", "Sam", "Dave", "Michael", "Matt", "Warner"]
name_having_4_letters = [name for name in names if len(name) <= 4]
print(name_having_4_letters)
print([name.upper() for name in names if len(name) > 4])
