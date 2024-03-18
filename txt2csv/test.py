import random

ENABLE_PLAYTEST = False
DEF_DIFFIC = 10

def create_guess(all_info, difficulty=DEF_DIFFIC):
    '''
    Takes information built up from past guesses that is stored in `all_info`,
    and uses it as guidance to generate a new guess of length `difficulty`.
    '''
    possible = [str(i) for i in range(10)] + [i for i in "+-%*="]
    possibles = [possible.copy() for i in range(difficulty)]
    for info in all_info:
        for num, color in enumerate(info):
            char = color[1]
            if color[-1] == 'green':
                possibles[num] = [char]
            else:
                if char in possibles[num]:
                    possibles[num].remove(char)
    return ''.join(random.choice(k) for k in possibles)
    pass


# Let's play a game of FoCdle... below we pass your `create_guess` function to
# our hidden `solve_FoCdle` function, which uses it to guess the secret in a
# game of FoCdle. This closely follows the program outline described in task 3.
# You may also call `solve_FoCdle` with `debug=True` to see printed information
# that corresponds with comments in that same outline.
#
# Note: When you click "Mark", the `solve_FoCdle` function is run 100 times
# with "25+4*12=73" as the secret, taking the average number of guesses
# required to solve it. The hidden assessment tests will use many different
# random secrets, so make sure you test your code beyond this example!

if ENABLE_PLAYTEST:  # Set to True to run this code when clicking "Run" in Grok
    secret = "25+4*12=73"
    nguesses, final_guess = solve_FoCdle(secret, create_guess, debug=False)
    print(f"Solved the FoCdle after {nguesses} guesses: '{final_guess}'")