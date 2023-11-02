# Write your code below this line 👇
def prime_checker(number):
    check = 0
    for i in range(2, 10):
        if number % i == 0 and i != number:
            check += 1
    if check == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)