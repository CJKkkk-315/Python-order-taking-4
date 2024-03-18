class Player:

    def __init__(self, name, played=0, won=0, lost=0, tied=0, current_points=100):
        self.name = name
        self.played = played
        self.won = won
        self.lost = lost
        self.tied = tied
        self.current_points = current_points

    def __str__(self):
        if self.played:
            return f'{self.name} has {self.current_points} points and a winning rate of {round(self.won/self.played * 100,1)}%.'
        else:
            return f'{self.name} has {self.current_points} points, and never played a game.'