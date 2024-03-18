import heapq
f = open('Astar.txt','w')
t = 0

def heuristic(square):
    target = 65
    diff = 0
    for i in range(5):
        diff += abs(target - sum(square[i * 5:(i + 1) * 5]))
        diff += abs(target - sum(square[i::5]))
    diff += abs(target - sum(square[::6]))
    diff += abs(target - sum(square[4:21:4]))
    global t
    print(square, '代价：', diff, end='   ')
    f.write(str(square) + str(diff) + '\n')
    t += 1
    if t == 10000:
        f.close()
        exit(0)
    return diff


def is_magic(square):
    if len(square) < 25:
        return False
    return heuristic(square) == 0


def print_square(square):
    for i in range(5):
        print(square[i * 5:(i + 1) * 5])


def a_star():
    start_node = ([], list(range(1, 26)), 0)  # square, available numbers, cost
    heap = []
    heapq.heappush(heap, (heuristic(start_node[0]) + start_node[2], start_node))

    while heap:
        _, (square, available_numbers, cost) = heapq.heappop(heap)

        if is_magic(square):
            print("Magic square found:")
            print_square(square)
            return

        for num in available_numbers:
            new_square = square + [num]
            new_available_numbers = [x for x in available_numbers if x != num]
            new_cost = cost + 1
            heapq.heappush(heap, (heuristic(new_square) + new_cost, (new_square, new_available_numbers, new_cost)))


# Start the search
print('A*搜索算法：')
a_star()
