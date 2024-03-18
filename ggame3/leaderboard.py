from player import Player
import os
class LeaderBoard:

    def __init__(self):
        self.__list_of_P = []

    def __sortPlayers(self):
        self.__list_of_P = sorted(self.__list_of_P, key=lambda x:x.S,reverse=True)

    def load(self):
        try:
            with open('player.txt') as f:
                lines = f.readlines()
                lines = [i.replace('\n','') for i in lines if i]
                i = 0
                while i < len(lines):
                    name = lines[i]
                    P, W, L, T, S = [int(i) for i in lines[i+1].split()]
                    player = Player(name, P, W, L, T, S)
                    self.__list_of_P.append(player)
                    i += 2
            self.__sortPlayers()
            return True
        except:
            return False

    def save(self):
        try:
            with open('player.txt','w') as f:
                for player in self.__list_of_P:
                    f.write(player.name)
                    f.write('\n')
                    f.write(str(player.P)+ ' ' + str(player.W)+ ' ' + str(player.L)+ ' ' + str(player.T)+ ' ' + str(player.S) + '\n')
            return True
        except:
            return False

    def display(self):
        if self.__list_of_P:
            print('|' + '-' * 58 + '|')
            print('|' + ' {:<30} {:>2} {:>2} {:>2} {:>2} {:>6} {:>6} '.format('Player Name','P','W','L','T','W-Rate','Points') + '|')
            print('|' + '-' * 58 + '|')
            for player in self.__list_of_P:
                if not player.P:
                    win_percent = 0
                else:
                    win_percent = player.W/player.P * 100
                print('|' + ' {:<30} {:>2} {:>2} {:>2} {:>2} {:>6} {:>6} '.format(player.name, player.P, player.W, player.L, player.T, '%0.1f' % win_percent + '%', player.S) + '|')
            print('|' + '-' * 58 + '|')
        else:
            print('|' + '-' * 58 + '|')
            print('|' + ' {:<30} {:>2} {:>2} {:>2} {:>2} {:>6} {:>6} '.format('Player Name', 'P', 'W', 'L', 'T', 'W-Rate','Points') + '|')
            print('|' + '-' * 58 + '|')
            print(
                '|' + '{:^58}'.format('No player to display.') + '|')
            print('|' + '-' * 58 + '|')

    def __findPlayer(self, name):
        names = [p.name for p in self.__list_of_P]
        if name in names:
            return True
        else:
            return False

    def addPlayer(self, name):
        if not self.__findPlayer(name):
            p = Player(name=name)
            self.__list_of_P.append(p)
            self.__sortPlayers()
            return True
        elif self.__findPlayer(name):
            return False

    def removePlayer(self, name):
        idx = None
        if self.__findPlayer(name):
            for p in self.__list_of_P:
                if p.name == name:
                    idx = self.__list_of_P.index(p)
            del self.__list_of_P[idx]
            return True
        elif not self.__findPlayer(name):
            return False

    def getPlayerPoints(self, name):
        idx = None
        if self.__findPlayer(name):
            for p in self.__list_of_P:
                if p.name == name:
                    idx = self.__list_of_P.index(p)
            return self.__list_of_P[idx].S
        elif not self.__findPlayer(name):
            return -1

    def getWinner(self):
        if self.__list_of_P:
            self.__sortPlayers()
            best_S = self.__list_of_P[0]
            return best_S
        else:
            return None

    def recordGamePlay(self, name, points, result):
        n = len(self.__list_of_P)
        for i in range(n):
            if self.__list_of_P[i].name == name:
                self.__list_of_P[i].P = self.__list_of_P[i].P + 1
                if result > 0:
                    self.__list_of_P[i].W = self.__list_of_P[i].W + 1
                    self.__list_of_P[i].S = self.__list_of_P[i].S + points
                elif result < 0:
                    self.__list_of_P[i].L = self.__list_of_P[i].L + 1
                    self.__list_of_P[i].S = self.__list_of_P[i].S - points
                elif result == 0:
                    self.__list_of_P[i].T += 1
        self.__sortPlayers()