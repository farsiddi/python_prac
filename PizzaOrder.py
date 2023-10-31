print("Thank you for choosing Python Pizza Deliveries! ")
size = input("Enter the size of the pizza: s , m or l ")
add_pepperoni = input("Want to add pepperoni: y or n ")
extra_cheese = input("Want to add extra cheese: y or n ")
bill = 0
if size == "s":
    bill = 15
    if add_pepperoni == "y":
        bill += 2
elif size == "m":
    bill = 20
    if add_pepperoni == "y":
        bill += 3
elif size == "l":
    bill = 25
    if add_pepperoni == "y":
        bill += 3

if extra_cheese == "y":
        bill += 1

print(f"Thank you for choosing Python Pizza. Your final bill is: ${bill}")