#
#COMP2034 Software Development
#Assignment 2
#Filename:game.py
#Module with the Game base class
#
#YOU MUST NOT MODIFY THIS FILE

class Game:
    '''Base class for all games.'''
    def __init__ (self):
      self.__debug_mode = False # Hidden attribute for debugMode
#Setter method fordebugMode
    def __setDebugMode(self,x):
      self.__debug_mode =x
# Getter method for debugMode
    def __getDebugMode(self):
       return self.__debug_mode
# Define property debugMode.
#If True,print computer's choice.
    debugMode=property(__getDebugMode,__setDebugMode)
#Play the game and return the result.
    def play(self):
        '''Play a round of game and return the result as:
        1 if the player win.
        -1 if the player lose.
        '''
        print("This game is not implemented.")
        return 0
