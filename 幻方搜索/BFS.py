from queue import Queue
f = open('bfs.txt','w')
t = 0
def is_magic(square):
    global t
    print(square,end='    ')
    f.write(str(square) + '\n')
    t += 1
    if t == 10000:
        f.close()
        exit(0)
    if len(square) < 25:
        return False
    target = 65
    for i in range(5):
        if sum(square[i * 5:(i + 1) * 5]) != target or sum(square[i::5]) != target:
            return False
    if sum(square[::6]) != target or sum(square[4:20:4]) != target:
        return False
    return True


def print_square(square):
    for i in range(5):
        print(square[i * 5:(i + 1) * 5])


def bfs():
    q = Queue()
    q.put(([], list(range(1, 26))))

    while not q.empty():
        square, available_numbers = q.get()

        if is_magic(square):
            print("Magic square found:")
            print_square(square)
            return

        for num in available_numbers:
            new_square = square + [num]
            new_available_numbers = [x for x in available_numbers if x != num]
            q.put((new_square, new_available_numbers))
print('BFS搜索：')
bfs()
