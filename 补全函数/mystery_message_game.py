"""Mystery Message main program."""

import random

from constants import (VOWEL_COST, CONSONANT_BONUS, PLAYER_ONE,
                       PLAYER_TWO, CONSONANT, VOWEL, SOLVE, QUIT,
                       HUMAN, HUMAN_HUMAN, HUMAN_COMPUTER, EASY, HARD,
                       ALL_CONSONANTS, ALL_VOWELS,
                       PRIORITY_CONSONANTS, HIDDEN)

import mm_functions as mmf


################################ The Game: #################################
def play_game(message: str, messages, game_type: str) -> None:
    """Play the game!"""

    view = make_view(message)
    consonants, vowels = ALL_CONSONANTS, ALL_VOWELS
    player_one_score, player_two_score = 0, 0
    current_player = PLAYER_ONE

    if game_type == HUMAN_COMPUTER:
        difficulty = select_computer_difficulty()

    move = ''
    while not mmf.is_game_over(view, message, move):
        score = mmf.current_player_score(player_one_score,
                                        player_two_score,
                                        current_player)
        num_occurrences = 0

        display_move_prompt(current_player, score, view)

        if mmf.is_human(current_player, game_type):
            (move, guess) = human_move(score, consonants, vowels)
        else:
            (move, guess) = computer_move(view, messages, difficulty,
                                          consonants)

        if move == QUIT:
            print('You chose to quit the game!')
            winner = 'No winner'

        elif move == SOLVE:
            if guess == message:
                score = compute_score(message, view, score)
                view = message
                winner = current_player
            else:
                print("The solution '{}' is incorrect. Keep playing!"
                      .format(guess))

        else:  # guess vowel or consonant
            view = update_view(message, view, guess)
            num_occurrences = message.count(guess)
            score = mmf.calculate_score(score, num_occurrences, move)

            consonants = mmf.erase(consonants, consonants.find(guess))
            vowels = mmf.erase(vowels, vowels.find(guess))

            winner = current_player

            print("{} guesses {}, which occurs {} time(s) in the message."
                  .format(current_player, guess, num_occurrences))
            print("{}'s score is now {}.".format(current_player, score))

        if current_player == PLAYER_ONE:
            player_one_score = score
        else:
            player_two_score = score
        current_player = mmf.next_player(
            current_player, num_occurrences, game_type)

    # The game is over.
    display_outcome(winner, message, game_type, player_one_score,
                    player_two_score)


def update_view(message: str, view: str, guess: str) -> str:
    """Return a new view of message: a view in which each occurrence of
    guessed_letter in message is revealed.

    >>> update_view('apple', '^^^le', 'a')
    'a^^le'
    >>> update_view('apple', '^^^le', 'p')
    '^pple'
    >>> update_view('apple', '^^^le', 'z')
    '^^^le'

    """

    new_view = ''
    for index in range(len(message)):
        new_view += mmf.get_updated_char_view(view, message, index, guess)
    return new_view


def compute_score(message: str, view: str, current_score: int) -> int:
    """Return the final score, calculated by adding
    constants.CONSONANT_BONUS points to current_score for each
    occurrence of a consonant in message that appears as
    consonants.HIDDEN in view.

    >>> compute_score('apple pies', '^pple p^es', 0)
    0
    >>> compute_score('apple pies', '^^^le ^^e^', 0)
    8

    """

    final_score = current_score
    for letter in ALL_CONSONANTS:
        if mmf.is_bonus_letter(view, letter, message):
            final_score += CONSONANT_BONUS * message.count(letter)
    return final_score


########################## Game Play: Computer Moves #######################
def computer_move(view: str, messages, difficulty: str,
                  consonants: str) -> (str, str):
    """Return the computer's next move:
    (constants.SOLVE, solution-guess) or (constants.CONSONANT, letter-guess)

    If difficulty is constants.HARD, the computer chooses to solve if
    at least half of the letters in view are revealed (not
    constants.HIDDEN). Otherwise, the computer opts to guess a
    consonant.

    """

    if mmf.computer_chooses_solve(view, difficulty, consonants):
        move = SOLVE
        guess = get_match(view, messages)
        print('\tI choose to solve: {}.'.format(guess))
    else:
        move = CONSONANT
        guess = computer_guess_letter(consonants, difficulty)
        print('\tI choose to guess letter: {}.'.format(guess))
    return move, guess


def get_match(view: str, messages) -> str:
    """Return a message from messages that could be represented by view. If
    no such message exists, return the empty string.

    >>> get_match('^^^ ro^k^', ['abc', 'csc rocks', 'math is cool'])
    'csc rocks'
    >>> get_match('^^^ ro^ks', ['abc', 'csc rocks', 'math is cool'])
    ''
    """

    for message in messages:
        if is_match(message, view):
            return message
    return ''


def is_match(message: str, view: str) -> bool:
    """Return True if and only if view is a valid message-view of message.

    >>> is_match('', '')
    True
    >>> is_match('a', 'a')
    True
    >>> is_match('bb', 'b^')
    False
    >>> is_match('abcde', 'ab^^e')
    True
    >>> is_match('axyzb', 'ab^^e')
    False
    >>> is_match('abcdefg', 'ab^^e')
    False

    """

    if len(message) != len(view):
        return False

    for index in range(len(message)):
        if (message[index] != view[index] and
                not mmf.is_fully_hidden(view, index, message)):
            return False
    return True


def computer_guess_letter(consonants: str, difficulty: str) -> str:
    """Return a letter from consonants. If difficulty is constants.EASY,
    select the letter randomly. If difficulty is constants.HARD,
    select the first letter from constants.PRIORITY_CONSONANTS that
    occurs in consonants.

    len(consonants) > 0;
    at least one character in consonants is in consonants.PRIORITY_CONSONANTS.
    difficulty in (constants.EASY, constants.HARD)

    >>> computer_guess_letter('bcdfg', 'H')
    'd'

    """

    if difficulty == HARD:
        for consonant in PRIORITY_CONSONANTS:
            if consonant in consonants:
                return consonant
    return random.choice(consonants)


########################## Game Play: User Interaction: ####################
def human_move(player_score: int, consonants: str, vowels: str) -> tuple:
    """Ask the user to make a complete move:

    1) Repeatedly ask to choose a move (constants.CONSONANT,
    constants.VOWEL, constants.SOLVE, or constants.QUIT), until a
    valid input is entered.

    2) Upon receiving constants.VOWEL or constants.CONSONANT,
    repeatedly prompt to choose a corresponding letter, until a valid
    input is entered.

    3) Upon receiving constants.SOLVE, prompt for a solution word.

    Return the user input guess, or the empty string is the first
    choice was constants.QUIT.

    """

    move = select_move(player_score, consonants, vowels)

    if move == QUIT:
        guess = ''
    if move == VOWEL:
        guess = select_letter(vowels)
    if move == CONSONANT:
        guess = select_letter(consonants)
    if move == SOLVE:
        guess = input('Input your solution guess: ')

    return (move, guess)


def select_move(score: int, consonants: str, vowels: str) -> str:
    """Repeatedly prompt current_player to choose a move until a valid
    selection is made. Return the selected move. Move validity is
    defined by is_valid_move(selected-move-type, score, consonants,
    vowels).

    (Note: Docstring examples not given since result depends on input
    data.)

    """

    prompt = make_move_prompt()

    move = input(prompt)
    while not is_valid_move(move.strip(), score, consonants, vowels):
        move = input(prompt)

    return move.strip()


def select_letter(letters: str) -> str:
    """Repeatedly prompt the user for a letter, until a valid input is
    received. Return the letter. Valid options are characters from
    letters.

    (Note: Docstring examples not given since result depends on input
    data.)

    """

    prompt = 'Choose a letter from [{}]: '.format(
        ','.join(['{}'] * len(letters)))
    valid_options = tuple(letters)
    return prompt_for_selection(prompt, valid_options)


def prompt_for_selection(prompt_format: str, valid_options: tuple) -> str:
    """Repeatedly ask the user for a selection, until one of valid_options
    is received. The user prompt is created as
    prompt_format.format(valid_option). Return the user input with
    leading and trailing whitespace removed.

    (Note: Docstring examples not given since result depends on input
    data.)

    """

    prompt = prompt_format.format(*valid_options)

    selection = input(prompt)
    while selection.strip() not in valid_options:
        selection = input('Invalid choice.\n{}'.format(prompt))

    return selection.strip()


def display_move_prompt(current_player: str, player_score: int,
                        view: str) -> None:
    """Display a prompt for the player to select the next move."""

    print('=' * 50)
    print('{}, it is your turn. You have {} points.'.format(
        current_player, player_score))
    print('\n' + view + '\n')


def make_move_prompt() -> str:
    """Return a prompt for the player to select the next move."""

    prompt = '''Select move type:
    [{}] - Vowel,
    [{}] - Consonant,
    [{}] - Solve,
    [{}] - Quit.\n'''.format(VOWEL, CONSONANT, SOLVE, QUIT)

    return prompt


def is_valid_move(move: str, score: int, consonants: str, vowels: str) -> bool:
    """Return whether move is valid. If invalid, print an explanatory
    message. A move is valid when:

    1) move is one of constants.CONSONANT, constants.VOWEL,
    constants.SOLVE, or constants.QUIT;

    2) If move is constants.VOWEL, score is high enough to buy a
    vowel(at least constants.VOWEL_COST), and vowels has at least
    one character.

    3) If move is constants.CONSONANT, consonants has at least
    one character.

    >>> is_valid_move('X', 0, '', '')
    Valid moves are: C, V, S, and Q.
    False
    >>> is_valid_move('Q', 0, '', '')
    True
    >>> is_valid_move('S', 42, 'bdfrt', 'aeui')
    True
    >>> is_valid_move('C', 2, 'bcdfghjklmnpqstvwxyz', 'aeiou')
    True
    >>> is_valid_move('C', 2, '', 'aeiou')
    You do not have any more consonants to guess!
    False
    >>> is_valid_move('V', 1, 'bcdfghjklmnpqstvwxyz', 'aeiou')
    True
    >>> is_valid_move('V', 0, 'bcdfghjklmnpqstvwxyz', 'aeiou')
    You do not have enough points to reveal a vowel. Vowels cost 1 point(s).
    False
    >>> is_valid_move('V', 42, 'bcdfghjklmnpqstvwxyz', '')
    You do not have any more vowels to guess!
    False

    """

    if move not in (CONSONANT, VOWEL, SOLVE, QUIT):
        print('Valid moves are: {}, {}, {}, and {}.'.format(
            CONSONANT, VOWEL, SOLVE, QUIT))
        return False

    if move == VOWEL and score < VOWEL_COST:
        print('You do not have enough points to reveal a vowel. '
              'Vowels cost {} point(s).'.format(VOWEL_COST))
        return False

    if move == VOWEL and vowels == '':
        print('You do not have any more vowels to guess!')
        return False

    if move == CONSONANT and consonants == '':
        print('You do not have any more consonants to guess!')
        return False

    return True


############################# Game Setup: #############################
def select_game_type() -> str:
    """Repeatedly prompt the user for game type, until a valid input is
    received. Return the game type. Valid options are constants.HUMAN,
    constants.HUMAN_HUMAN, and constants.HUMAN_COMPUTER.

    (Note: Docstring examples not given since result depends on input
    data.)

    """

    prompt = '''Choose the game type:
     [{}] - One Player
     [{}] - Human-human
     [{}] - Human-computer\n'''
    valid_options = HUMAN, HUMAN_HUMAN, HUMAN_COMPUTER
    return prompt_for_selection(prompt, valid_options)


def select_computer_difficulty() -> str:
    """Repeatedly prompt the user for computer difficulty, until a valid
    input is received. Return the computer difficulty. Valid options
    are constants.EASY and constants.HARD.

    (Note: Docstring examples not given since result depends on input
    data.)

    """

    prompt = 'Choose the game difficulty ([{}] - Easy or [{}] - Hard): '
    valid_options = EASY, HARD
    return prompt_for_selection(prompt, valid_options)


def make_view(message: str) -> str:
    """Return a string that is based on message, with each alphabetic
    character replaced by the constants.HIDDEN character.

    >> > make_view('apple cake is great! #csc108')
    '^^^^^ ^^^^ ^^ ^^^^^! #^^^108'
    >> > make_view('108@#$&')
    '108@#$&'

    """

    view = ''
    for char in message:
        if char.isalpha():
            view = view + HIDDEN
        else:
            view = view + char
    return view


############################# Game Over: #############################
def display_outcome(winner: str, message: str, game_type: str,
                    player_one_score: int, player_two_score: int) -> None:
    """Display the outcome of game: who won and what the final scores are.
    """

    print('And the winner is... {}!'.format(winner))
    print('The solution to this game\'s message is: {}.'.format(message))
    if mmf.is_one_player_game(game_type):
        print('In this game, the player scored {} point(s)'.
              format(player_one_score))
    else:
        print('In this game, {} scored {} and {} scored {} point(s)'.
              format(PLAYER_ONE, player_one_score, PLAYER_TWO,
                     player_two_score))


############################# The Program: #############################
if __name__ == '__main__':

    import doctest
    doctest.testmod()

    DATA_FILE = 'messages_small.txt'

    PUZZLES = []
    with open(DATA_FILE) as data_file:
        for line in data_file:
            PUZZLES.append(line.lower().strip())

    PUZZLE = random.choice(PUZZLES)

    print('Welcome to the Mystery Message Game!')

    print('***' + PUZZLE + '***')

    GAME_TYPE = select_game_type()
    play_game(PUZZLE, PUZZLES, GAME_TYPE)
