import game
import random
class Inbetween(game.Game):
    def __init__(self):
        super().__init__()

    def play(self):
        print("Let's play In-between!")
        start = 0
        end = 0
        while start == end or 9 <= abs(start - end) or abs(start - end) <= 1:
            start = random.randint(1, 10)
            end = random.randint(1, 10)
        if start - end > 0:
            start, end = end, start
        if self.debugMode:
            print(f"DEBUG: {start} - {end}")
        while True:
            user_number = int(input('Choose a number (1-10): '))
            if 1 <= user_number <= 10:
                break
        print(f'Computer chose {start} and {end}, you chose {user_number}')
        if start < user_number < end:
            print('You win!')
            return 1
        elif user_number == start or user_number == end:
            print('Tie!')
            return 0
        else:
            print('You lose!')
            return -1



