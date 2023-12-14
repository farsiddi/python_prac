num = input("Enter a number")
if num == num[::-1]:
    print("Yes its a palindrome")
else:
    print("No, its not a palindrome")

# num = is string that's the problem


n = int(input("Enter number:"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
