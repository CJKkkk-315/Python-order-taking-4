"""CSC108/CSCA08: Fall 2022 -- Assignment 1: Mystery Message Game

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2022 Mario Badr, Jennifer Campbell, Tom Fairgrieve, Diane
Horton, Michael Liut, Jacqueline Smith, Anya Tafliovich and Michelle Craig.
"""

from constants import (CONSONANT_POINTS, VOWEL_COST, CONSONANT_BONUS,
                       PLAYER_ONE, PLAYER_TWO, CONSONANT, VOWEL,
                       SOLVE, QUIT, HUMAN, HUMAN_HUMAN,
                       HUMAN_COMPUTER, EASY, HARD, ALL_CONSONANTS,
                       ALL_VOWELS, PRIORITY_CONSONANTS, HIDDEN)

# We provide this function as an example.
def is_win(view: str, message: str) -> bool:
    """Return True if and only if message and view are a winning
    combination. That is, if and only if message and view are the same.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('a^^le', 'apple')
    False
    >>> is_win('app', 'apple')
    False
    """

    return message == view


# We provide this function as an example of using a function as a helper.
def is_game_over(view: str, message: str, move: str) -> bool:
    """Return True if and only if message and view are a winning
    combination or move is QUIT.

    >>> is_game_over('a^^le', 'apple', 'V')
    False
    >>> is_game_over('a^^le', 'apple', 'Q')
    True
    >>> is_game_over('apple', 'apple', 'S')
    True
    """

    return move == QUIT or is_win(view, message)

def is_one_player_game(game_type):

# We provide the header and docstring of this function as an example
# of where and how to use constants in the docstring.
def is_human(current_player: str, game_type: str) -> bool:
    """Return True if and only if current_player represents a human in a
    game of type game_type.

    current_player is PLAYER_ONE or PLAYER_TWO.
    game_type is HUMAN, HUMAN_HUMAN, or HUMAN_COMPUTER.

    In a HUMAN game or a HUMAN_HUMAN game, a player is always
    human. In a HUMAN_COMPUTER game, PLAYER_ONE is human and
    PLAYER_TWO is computer.

    >>> is_human('Player One', 'P1')
    True
    >>> is_human('Player One', 'PVP')
    True
    >>> is_human('Player Two', 'PVP')
    True
    >>> is_human('Player One', 'PVE')
    True
    >>> is_human('Player Two', 'PVE')
    False
    """
    
    if current_player == 'Player One':
        return game_type == 'P1' or 'PVP' or 'PVE'
    if current_player == 'Player Two':
        return game_type == 'PVP'


# Helper function for computer_chooses_solve
# This function is already complete. You must not modify it.
def half_revealed(view: str) -> bool:
    """Return True if and only if at least half of the alphabetic
    characters in view are revealed.

    >>> half_revealed('')
    True
    >>> half_revealed('x')
    True
    >>> half_revealed('^')
    False
    >>> half_revealed('a^,^c!')
    True
    >>> half_revealed('a^b^^e ^c^d^^d')
    False
    """

    num_hidden = view.count(HIDDEN)
    num_alphabetic = 0
    for char in view:
        if char.isalpha():
            num_alphabetic += 1
    return num_alphabetic >= num_hidden


def is_one_player_game(view:str) -> bool:
    """Return True if and only if the view is a one-player game.
    
    >>> is_one_player_game('Player One')
    True
    >>> is_one_player_game('Player Two')
    False
    """
    
    return view == 'Player One'


def current_player_score(score_of_player_one: int, score_of_player_two: int, current_player: str) -> int:
    """Return the score of the current player with the score of player one and
    the score of player two.
    
    >>> current_player_score(2, 3, 'Player One')
    2
    >>> current_player_score(2, 4, 'Player Two')
    4
    """
    
    if current_player == 'Player One':
        return score_of_player_one
    else:
        return score_of_player_two
   

def is_bonus_letter(view: str, letter: str, message: str) -> bool:
    """Return True if and only if the letter is a bonus letter with view
    and message.
    
    Precondition: 'bonus_letter' = 'p'
    
    >>> is_bonus_letter('a^^le', 'p', 'apple')
    True
    >>> is_bonus_letter('a^^le', 'i', 'apple')
    False
    """
    
    return letter == "bonus_letter"


def get_updated_char_view(view: str, message: str, the_index_of_a_char: int, guess_for_char: str) -> str:
    """Return a single character string that is the updated view of that 
    one character.
    
    >>> get_updated_char_view('a^^^e', 'apple', 3, 'l')
    'a^^le'
    >>> get_updated_char_view('a^^^e', 'apple', 3, 'b')
    'a^^^e'
    """
    
    if guess_for_char in message:
        return get_updated_char_view