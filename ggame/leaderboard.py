from player import Player
class LeaderBoard:

    def __init__(self):
        self.__player_list = []

    def __sortPlayers(self):
        self.__player_list.sort(key=lambda x:x.current_points,reverse=True)

    def load(self):
        try:
            f = open('player.txt')
            data = [i for i in f.read().split('\n') if i]
            for i in range(0,len(data),2):
                name = data[i]
                played, won, lost, tied, current_points = [int(i) for i in data[i+1].split()]
                self.__player_list.append(Player(name, played, won, lost, tied, current_points))
            self.__sortPlayers()
            f.close()
            return True
        except:
            return False

    def save(self):
        try:
            f = open('player.txt','w')
            for player in self.__player_list:
                f.write(player.name + '\n')
                f.write(' '.join(list(map(str,[player.played, player.won, player.lost,
                                               player.tied, player.current_points]))) + '\n')
            f.close()
            return True
        except:
            return False

    def display(self):
        print('|' + '-' * 58 + '|')
        print('|' + ' {:<30} {:<2} {:<2} {:<2} {:<2} {:<6} {:<6} '.format('Player Name','P','W','L','T','W-Rate','Points') + '|')
        print('|' + '-' * 58 + '|')
        for player in self.__player_list:
            if player.played == 0:
                wr = 0
            else:
                wr = player.won/player.played * 100
            print('|' + ' {:<30} {:<2} {:<2} {:<2} {:<2} {:<6} {:<6} '.format(player.name, player.played, player.won, player.lost, player.tied, '%0.1f' % wr + '%' ,player.current_points) + '|')
        print('|' + '-' * 58 + '|')

    def __findPlayer(self, name):
        return name in [player.name for player in self.__player_list]

    def addPlayer(self, name):
        if not self.__findPlayer(name):
            self.__player_list.append(Player(name))
            self.__sortPlayers()
            return True
        else:
            return False

    def removePlayer(self, name):
        if self.__findPlayer(name):
            target = [player for player in self.__player_list if player.name == name][0]
            self.__player_list.remove(target)
            return True
        else:
            return False

    def getPlayerPoints(self, name):
        if self.__findPlayer(name):
            target = [player for player in self.__player_list if player.name == name][0]
            return target.current_points
        else:
            return -1

    def getWinner(self):
        if self.__player_list:
            self.__sortPlayers()
            return self.__player_list[0]
        else:
            return None

    def recordGamePlay(self, name, points, result):
        for i in range(len(self.__player_list)):
            if self.__player_list[i].name == name:
                self.__player_list[i].played += 1
                if result == 1:
                    self.__player_list[i].won += 1
                    self.__player_list[i].current_points += points
                elif result == -1:
                    self.__player_list[i].lost += 1
                    self.__player_list[i].current_points -= points
                else:
                    self.__player_list[i].tied += 1

        self.__sortPlayers()