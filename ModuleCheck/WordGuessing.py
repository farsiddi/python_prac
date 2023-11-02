import random

word_list = ["forest", "bottle", "sunlight", "computer"]
word = random.choice(word_list)
print(word)

letter = input("Guess a letter")

for wd in word:
    if wd == letter:
        print("right")
    else:
        print("wrong")
