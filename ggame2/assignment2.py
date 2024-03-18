#
# COMP2034 Software Development
# Assignment 2
# Filename: assignment2.py
# Main file that imports other modules and runs the program.
#
# YOU MUST NOT MODIFY THIS FILE.
#

import rpsgame
import inbetweengame
import leaderboard

# Create an instance of a LeaderBoard class.
leaderBoard = leaderboard.LeaderBoard()

# Load data from file.
if leaderBoard.load() == True:
    print("Players info successfully loaded.")
else:
    print("ERROR: Cannot load players info.")
print()

# Command prompt loop.
command = ""
while command != "quit":
    command = input("Please enter a command [list, add, remove, play, winner, quit]: ")

    # list command
    if command == "list":
        leaderBoard.display()
    # add command
    elif command == "add":
        name = input("Name: ")
        if leaderBoard.addPlayer(name) == True:
            print(f"Successfully added player {name}.")
        else:
            print(f"Player {name} already exists.")
    # remove command
    elif command == "remove":
        name = input("Name: ")
        if leaderBoard.removePlayer(name) == True:
            print(f"Successfully removed player {name}.")
        else:
            print("No such player found.")
    # play command
    elif command == "play":
        # Ask player name.
        name = input("Name: ")
        points = leaderBoard.getPlayerPoints(name)
        if points < 0:
            print("No such player found.")
        elif points == 0:
            print("Not enough points to play.")
        else:
            # Ask points to bid.
            if points == 1:
                bid = 1
                print("Bidding one last point.")
            else:
                bid = 0
                while bid <= 0 or bid > points:
                    try:
                        bid = int(input(f"How many points to bid (1-{points})? "))
                    except:
                        bid = 0

            # Ask game to play.
            gameChoice = ""
            while gameChoice not in ['r', 'i']:
                gameChoice = input("Which game ([r]Rock-Paper-Scissors, [i]In-between)? ")

            # Play game.
            if gameChoice == 'r':
                game = rpsgame.RockPaperScissors()
            else:
                game = inbetweengame.Inbetween()
            game.debugMode = True
            result = game.play()

            # Record the game result to the leader board.
            leaderBoard.recordGamePlay(name, bid, result)

            # Report on the points left
            points = leaderBoard.getPlayerPoints(name)
            if result == 0:
                print("No changes to your points.")
            elif points == 0:
                print("Oh no! You ran out of points!")
            elif points == 1:
                print("You now have only 1 point left.")
            else:
                print(f"You now have {points} points.")
    # winner command
    elif command == "winner":
        winner = leaderBoard.getWinner()
        if winner == None:
            print("There is no winner.")
        else:
            print(winner)
    # quit command
    elif command == "quit":
        print("Thank you for playing!")
        print()
        # Save data to file.
        if leaderBoard.save() == True:
            print("Players info successfully saved.")
        else:
            print("ERROR: Cannot save players info.")
    else:
        print(f"Invalid command: {command}")

    print()
