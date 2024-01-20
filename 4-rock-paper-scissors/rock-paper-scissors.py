import random


def play():
    userChoice = input(
        "Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors \n"
    )

    computerChoice = random.choice(["r", "p", "s"])

    if userChoice == computerChoice:
        return "It's a tie"

    if isWin(userChoice, computerChoice):
        return "You Won!"

    return "You Lost"


def isWin(player, opponent):
    # return true if player wins
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())
