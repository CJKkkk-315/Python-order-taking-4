import game
import random

class Inbetween(game.Game):
    def __init__(self):
        super().__init__()

    def play(self):
        print("Let's play In-between!")
        a, b = 0, 0
        while a == b or abs(a - b) == 1:
            a, b = random.randint(1, 10), random.randint(1, 10)
        if a > b:
            a, b = b, a
        if self.debugMode:
            print(f"DEBUG: {a} - {b}")
        while True:
            c = int(input('Choose a number (1-10): '))
            if c < 1 or c > 10:
                continue
            break
        print(f'Computer chose {a} and {b}, you chose {c}')
        if c == a or c == b:
            print('Tie!')
            return 0
        elif a < c < b:
            print('You win!')
            return 1
        else:
            print('You lose!')
            return -1



