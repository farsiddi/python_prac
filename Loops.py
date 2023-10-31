places = ["Kashmir", "Himachal", "Assam", "Nagpur", "Lucknow", "Mumbai", "Lucknow"]
for place in places:
    print(place)

# range(start , end , steps)
for number in range(1, 20):  # Does not include the last index
    print(number)

for number in range(1, 20, 4):  # After every 4 steps
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

# while vs for -