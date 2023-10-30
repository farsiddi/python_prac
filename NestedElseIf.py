print("Welcome to the Roller coaster")
height = int(input("Enter your height"))
age = int(input('Enter your age'))
if height >= 120:
    if age > 18:
        print("You can enter")
    elif age == 18:
        print("You can enter")
    else:
        print("You can not enter")
else:
    print("You can not enter")