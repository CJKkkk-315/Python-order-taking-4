#
# COMP2034 Software Development
# Assignment 2
# Filename: rpsgame.py
# Module with RockPaperScissors game class.
#
# YOU MUST NOT MODIFY THIS FILE.
#

import random
import game


class RockPaperScissors(game.Game):
    """ Rock-Paper-Scissors game class"""

    def __init__(self):
        super().__init__()  # Call initialiser of the super class.

    # This method is overrided from the base class.
    def play(self):
        print("Let's play Rock-Paper-Scissors!");

        # Define code for the game.
        rpsCode = ["r", "p", "s"]
        rpsCodeToStr = {
            "r": "rock",
            "p": "paper",
            "s": "scissors"
        }

        # Make random choice by the computer.
        computerChoice = random.choice(rpsCode)

        # Print computer choice if in debug mode.
        if self.debugMode == True:
            print(f"DEBUG: Computer chose {rpsCodeToStr[computerChoice]}.")

        # Get player choice.
        playerChoice = ""  # Choice made by the player.
        while playerChoice not in rpsCode:
            playerChoice = input("What is your choice (r: rock / p: paper / s: scissors)? ")

        # Decide the game outcome.
        print(f"Computer chose {rpsCodeToStr[computerChoice]}, you chose {rpsCodeToStr[playerChoice]}.")
        gameResult = 0  # Outcome of the game: 1 if player won, -1 if player lose, 0 if draw.
        if playerChoice == 'r':
            if computerChoice == 'r':
                gameResult = 0
            elif computerChoice == 'p':
                gameResult = -1
            else:  # computerChoice == 's'
                gameResult = 1
        elif playerChoice == 'p':
            if computerChoice == 'r':
                gameResult = 1
            elif computerChoice == 'p':
                gameResult = 0
            else:  # computerChoice == 's'
                gameResult = -1
        else:  # This is when playerChoice is 's'.
            if computerChoice == 'r':
                gameResult = -1
            elif computerChoice == 'p':
                gameResult = 1
            else:  # computerChoice == 's'
                gameResult = 0

        # Print out the result.
        if gameResult > 0:
            print("You win!")
        elif gameResult < 0:
            print("You lose!")
        else:
            print("Tie!")

        return gameResult


# Testing RockPaperScissors class.
if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.debugMode = True

    repeat = 'y'
    while repeat == 'y':
        res = rps.play()
        print("Return value", res)
        repeat = input("Play again (y/n)? ")
