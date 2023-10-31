start = int(input("Enter the starting point number: \n"))
end =int(input("Enter the endind point number: \n"))
total = 0
for number in range(start, end+1):
    if number % 2 ==0:
        total += number

print(total)