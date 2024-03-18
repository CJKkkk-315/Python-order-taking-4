"""
A Python module for the Gomoku game.
TODO: Add a description of the module.

Full name: Peter Pan
StudentId: 123456
Email: peter.pan@student.manchester.ac.uk
"""

from copy import deepcopy  # you may use this for copying a board


def newGame(player1, player2):
    """
    TODO in Task 1. Write meaningful docstring!
    """
    game = {
        'player1': player1,
        'player2': player2,
        'who': 1,
        'board': [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]
    }

    return game


# TODO: All the other functions of Tasks 2-11 go here.
# USE EXACTLY THE PROVIDED FUNCTION NAMES AND VARIABLES!


def posToIndex(s):
    s = s.replace(' ','').lower()
    if len(s) > 2:
        raise ValueError
    if s[0].isalpha():
        c = ord(s[0]) - 97
        r = int(s[1]) - 1
    else:
        c = ord(s[1]) - 97
        r = int(s[0]) - 1
    if r >= 8 or c >= 8:
        raise ValueError
    return (r,c)

def indexToPos(t):
    number = str(t[0] + 1)
    alpha = chr(t[1]+97)
    return alpha + number
def printBoard(board):
    print(' |a|b|c|d|e|f|g|h|')
    print(' +-+-+-+-+-+-+-+-+')
    for i in range(len(board)):
        display_row = []
        for j in range(len(board[i])):
            if board[i][j] == 1:
                display_row.append('X')
            elif board[i][j] == 2:
                display_row.append('O')
            else:
                display_row.append(' ')
        print(str(i+1) + '|',end='')
        print('|'.join(display_row) + '|')
    print(' +-+-+-+-+-+-+-+-+')
def loadGame(filename):
    try:
        f = open(filename)
        content = f.read().split('\n')
        f.close()
    except:
        raise FileNotFoundError

    try:
        player1 = content[0]
        player2 = content[1]
        who = content[2]
        board = []
        for i in range(3,11):
            row = list(map(int,content[i].split(',')))
            if len(row) != 8:
                raise ValueError
            board.append(row)
        game = {
            'player1': player1,
            'player2': player2,
            'who': who,
            'board': board
        }
        return game
    except:
        raise ValueError
def getValidMoves(board):
    res = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                res.append((i,j))
    return res
def makeMove(board,move,who):
    board[move[0]][move[1]] = who
    return board
def hasWon(board,who):
    size = len(board)
    for x in range(size - 4):
        for y in range(size):
            if board[x][y] == who and board[x + 1][y] == who and board[x + 2][y] == who and \
                    board[x + 3][y] == who and board[x + 4][y] == who:
                return True
    for x in range(size):
        for y in range(size - 4):
            if board[x][y] == who and board[x][y + 1] == who and board[x][y + 2] == who and \
                    board[x][y + 3] == who and board[x][y + 4] == who:
                return True

    for x in range(size - 4):
        for y in range(size - 4):
            if board[x][y] == who and board[x + 1][y + 1] == who and board[x + 2][y + 2] == who and \
                    board[x + 3][y + 3] == who and board[x + 4][y + 4] == who:
                return True

    for x in range(size - 4):
        for y in range(size - 4):
            if board[x + 4][y] == who and board[x + 3][y + 1] == who and board[x + 2][y + 2] == who and \
                    board[x + 1][y + 3] == who and board[x][y + 4] == who:
                return True
    return False
def suggestMove1(board,who):
    if who == 1:
        vs = 2
    else:
        vs = 1
    board2 = deepcopy(board)
    valid_moves = getValidMoves(board2)
    for pos in valid_moves:
        board2[pos[0]][pos[1]] = who
        if hasWon(board2,who):
            return pos
        board2[pos[0]][pos[1]] = 0
    for pos in valid_moves:
        board2[pos[0]][pos[1]] = vs
        if hasWon(board2,vs):
            return pos
        board2[pos[0]][pos[1]] = 0
    return valid_moves[0]
# ------------------- Main function --------------------

def play():
    """
    TODO in Task 10. Write meaningful docstring!
    """
    print("*" * 55)
    print("***" + " " * 8 + "WELCOME TO STEFAN'S GOMOKU!" + " " * 8 + "***")
    print("*" * 55, "\n")
    print("Enter the players' names, or type 'C' or 'L'.\n")
    # TODO: Game flow control starts here
    game = None
    while True:
        player1 = input("player1' name:")
        if player1 == '':
            print('name must be a nonempty string')
            continue
        if player1 == 'L':
            filename = input("Please Enter File Name:")
            if filename == '':
                filename = 'game.txt'
            game = loadGame(filename)
            player1 = game['player1']
            player2 = game['player2']
            break
        player2 = input("player2' name:")
        if player2 == '':
            print('name must be a nonempty string')
            continue
        break
    player1 = player1[0].upper() + player1[1:]
    player2 = player2[0].upper() + player2[1:]
    if game is None:
        game = newGame(player1,player2)
    while True:
        printBoard(game['board'])
        if hasWon(game['board'], 1):
            print('Player 1, you win!')
            break
        if hasWon(game['board'], 2):
            print('Player 2, you win!')
            break
        valid_moves = getValidMoves(game['board'])
        if len(valid_moves) == 0:
            print('It ends in a draw!')
            break
        if game['who'] == 1:
            if game['player1'] == 'C':
                idx = suggestMove1(game['board'],game['who'])
                game['board'] = makeMove(game['board'], idx, game['who'])
                game['who'] = 2
            else:
                pos = input('Player 1, please enter the location you want:')
                idx = posToIndex(pos)
                if idx not in valid_moves:
                    print('Invalid position!')
                    continue
                game['board'] = makeMove(game['board'],idx,game['who'])
                game['who'] = 2

        else:
            if game['player2'] == 'C':
                idx = suggestMove1(game['board'], game['who'])
                game['board'] = makeMove(game['board'], idx, game['who'])
                game['who'] = 1
            else:
                pos = input('Player 2, please enter the location you want:')
                idx = posToIndex(pos)
                if idx not in valid_moves:
                    print('Invalid position!')
                    continue
                game['board'] = makeMove(game['board'], idx, game['who'])
                game['who'] = 1

# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    play()