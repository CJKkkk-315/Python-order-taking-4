#
# COMP2034 Software Development
# Assignment 2
# Filename: game.py
# Module with the Game base class.
#
# YOU MUST NOT MODIFY THIS FILE.
#

class Game:
    """ Base class for all games."""

    def __init__(self):
        self.__debug_mode = False  # Hidden attribute for debugMode.

    # Setter method for __debugMode.
    def __setDebugMode(self, x):
        self.__debug_mode = x

    # Getter method for __debugMode.
    def __getDebugMode(self):
        return self.__debug_mode

    # Define property debugMode.
    # If True, print computer's choice.
    debugMode = property(__getDebugMode, __setDebugMode)

    # Play the game and return the result.
    def play(self):
        """ Play a round of game and return the result as:
            1 if the player win.
            -1 if the player lose.
            0: if it is a draw.
        """
        print("This game is not implemented.")
        return 0


