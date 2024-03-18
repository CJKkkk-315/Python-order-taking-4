f = open('dfs.txt','w')
t = 0


def is_magic(square):
    global t
    print(square)
    f.write(str(square) + '\n')
    t += 1
    if t == 10000:
        f.close()
        exit(0)
    target = 65
    for i in range(5):
        if sum(square[i * 5:(i + 1) * 5]) != target or sum(square[i::5]) != target:
            return False
    if sum(square[::6]) != target or sum(square[4:21:4]) != target:
        return False
    return True


def dfs(square, available_numbers):
    if len(square) == 25:
        if is_magic(square):
            print("Magic square found:")
            for i in range(5):
                print(square[i * 5:(i + 1) * 5])
            return True
        else:
            return False

    for num in available_numbers:
        square.append(num)
        if dfs(square, [x for x in available_numbers if x != num]):
            return True
        square.pop()

    return False

print('DFS搜索：')
available_numbers = list(range(1, 26))
dfs([], available_numbers)
