import random

word_list = ["forest", "bottle", "sunlight", "computer"]
word = random.choice(word_list)
print(word)

display = []
for i in word:
    display += "_"
print(display)
lives = 3

at_end = False

while not at_end:
    guess_letter = input("Enter the letter: \n").lower()

    i = 0
    for char in word:
        if char == guess_letter:
            display[i] = guess_letter
        i += 1

    if guess_letter not in word:
        lives -= 1
        # print(f"You are left with {lives}")
        if lives == 0:
            at_end = True
            print("You Lose")

    print(display)

    if "_" not in display:
        at_end = True
        print("You win")
