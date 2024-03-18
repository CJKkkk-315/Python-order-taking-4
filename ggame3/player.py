class Player:

    def __init__(self, name, P=0, W=0, L=0, T=0, S=100):
        self.name = name
        self.P = P
        self.W = W
        self.L = L
        self.T = T
        self.S = S

    def __str__(self):
        if self.P:
            R = round(self.W/self.P * 100, 1)
            return f'{self.name} has {self.S} points and a winning rate of {R}%.'
        else:
            return f'{self.name} has {self.S} points, and never played a game.'