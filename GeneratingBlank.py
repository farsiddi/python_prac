import random

word_list = ["forest", "bottle", "sunlight", "computer"]
word = random.choice(word_list)
print(word)

letter = input("Guess a letter")

# for wd in word:
#     if wd == letter:
#         print("right")
#     else:
#         print("wrong")
guess_list = []
length = len(word)
for num in range(length):
    guess_list.append("_")
print(guess_list)

# display = []
# for i in word:
#     display += "_"
# print(display)
# for position in range(len(word)):
#     letter = word[position]
#     if word == letter:
#         display += letter

i = 0
for char in word:
    if char == letter:
        guess_list[i] = letter
    i += 1
print(guess_list)
