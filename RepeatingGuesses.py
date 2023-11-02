import random

word_list = ["forest", "bottle", "sunlight", "computer"]
word = random.choice(word_list)
print(word)

display = []
for i in word:
    display += "_"
print(display)

at_end = False

while not at_end:
    guess_letter = input("Enter the letter: \n")

    i = 0
    for char in word:
        if char == guess_letter:
            display[i] = guess_letter
        i += 1
    print(display)

    if "_" not in display:
        at_end = True
        print("You win")

