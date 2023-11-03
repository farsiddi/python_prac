import os

print("Welcome to the auction")
bids = {}


def highest_bidder(bidder_details):
    highest_amt = -1
    winner = ""
    for bidder in bidder_details:
        bid_amount = bidder_details[bidder]
        if bid_amount > highest_amt:
            highest_amt = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the amount is {highest_amt}")


while True:
    next_bidder = input("Is there a new bidder- yes or no\n").lower()
    if next_bidder == "no":
        highest_bidder(bids)
        break
    elif next_bidder == "yes":
        name = input('Enter your name:\n')
        bid_amt = int(input("Enter the bid amount\n"))
        bids[name] = bid_amt