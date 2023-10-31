import random
names_string = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# The code above converts the input into an array separating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

length_names = len(names_string) - 1
payee_name = random.randint(0, length_names)
name = names_string[payee_name]
print(f"{name} is going to buy the meal today!")
