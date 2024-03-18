from player import Player
import os
class LeaderBoard:

    def __init__(self):
        self.__players = []

    def __sortPlayers(self):
        self.__players.sort(key=lambda x:x.points)
        self.__players = self.__players[::-1]

    def load(self):
        if os.path.exists('player.txt'):
            with open('player.txt') as f:
                fd = []
                for i in f.read().split('\n'):
                    if i != '':
                        fd.append(i)
                for i in range(0,len(fd),2):
                    name = fd[i]
                    played, won, lost, tied, points = [int(i) for i in fd[i+1].split()]
                    player = Player(name, played, won, lost, tied, points)
                    self.__players.append(player)
            self.__sortPlayers()
            return True
        else:
            return False

    def save(self):
        try:
            with open('player.txt','w') as f:
                for player in self.__players:
                    f.write(player.name)
                    f.write('\n')
                    res_str = ' '.join([str(player.played), str(player.won), str(player.lost), str(player.tied), str(player.points)])
                    f.write(res_str)
                    f.write('\n')
            return True
        except:
            return False

    def display(self):
        print('|' + '-' * 58 + '|')
        print('|' + ' {:<30} {:>2} {:>2} {:>2} {:>2} {:>6} {:>6} '.format('Player Name','P','W','L','T','W-Rate','Points') + '|')
        print('|' + '-' * 58 + '|')
        for player in self.__players:
            if player.played == 0:
                rate = 0
            else:
                rate = player.won/player.played * 100
            print('|' + ' {:<30} {:>2} {:>2} {:>2} {:>2} {:>6} {:>6} '.format(player.name, player.played, player.won, player.lost, player.tied, '%0.1f' % rate + '%' ,player.points) + '|')
        print('|' + '-' * 58 + '|')

    def __findPlayer(self, name):
        for player in self.__players:
            if player.name == name:
                return True
        return False

    def addPlayer(self, name):
        if self.__findPlayer(name) == False:
            player = Player(name=name)
            self.__players.append(player)
            self.__sortPlayers()
            return True
        else:
            return False

    def removePlayer(self, name):
        if self.__findPlayer(name) == True:
            for player in self.__players:
                if player.name == name:
                    need_remove = player
            self.__players.remove(need_remove)
            return True
        else:
            return False

    def getPlayerPoints(self, name):
        if self.__findPlayer(name) == True:
            for player in self.__players:
                if player.name == name:
                    need_points = player
            return need_points.points
        else:
            return -1

    def getWinner(self):
        if self.__players:
            self.__sortPlayers()
            winner = self.__players[0]
            return winner
        else:
            return None

    def recordGamePlay(self, name, points, result):
        points = points * result
        for iteration in range(len(self.__players)):
            if self.__players[iteration].name == name:
                self.__players[iteration].played += 1
                if result == 1:
                    self.__players[iteration].won += 1
                    self.__players[iteration].points += points
                elif result == -1:
                    self.__players[iteration].lost += 1
                    self.__players[iteration].points += points
                else:
                    self.__players[iteration].tied += 1
        self.__sortPlayers()