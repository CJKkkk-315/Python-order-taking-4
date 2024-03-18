class Player:

    def __init__(self, name, played=0, won=0, lost=0, tied=0, points=100):
        self.name = name
        self.played = played
        self.won = won
        self.lost = lost
        self.tied = tied
        self.points = points

    def __str__(self):
        if self.played:
            rate = self.won/self.played * 100
            return f'{self.name} has {self.points} points and a winning rate of {round(rate,1)}%.'
        else:
            return f'{self.name} has {self.points} points, and never played a game.'