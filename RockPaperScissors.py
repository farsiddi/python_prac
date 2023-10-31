import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
graphics = [rock, paper, scissors]

print("Welcome to the Rock Paper Scissors game")
points = 0
user_in = int(input("Press 0 for Rock , 1 for Paper , 2 for Scissors"))
comp_in = random.randint(0, 2)
print(graphics[user_in])

if comp_in == user_in:
    print("Its a draw")
elif comp_in == 0 and user_in == 1 or comp_in == 1 and user_in == 0:
    print("You won")
elif comp_in == 0 and user_in == 2 or comp_in == 2 and user_in == 0:
    print("Computer won")
elif comp_in == 1 and user_in == 2 or comp_in == 2 and user_in == 1:
    print("You won")
