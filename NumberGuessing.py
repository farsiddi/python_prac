from random import randint

easy_level = 10
hard_level = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """It checks answer that it matches with guess and returns the number of turns remaining."""
    if guess > answer:
        print("The guessed number is too high.")
        return turns - 1
    elif guess < answer:
        print("The guessed number is too low.")
        return turns - 1
    else:
        print(f"You guessed the correct answer- {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level


def game():
    # Chooses a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(answer)

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You Lost.")
            return
        elif guess != answer:
            print("Guess again.")


game()
