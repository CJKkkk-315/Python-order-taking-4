M = 99999


def construct_graph(file_path):
    with open(file_path) as f:
        file_data = f.read().split('\n')
    max_n = -1
    data = []
    for i in file_data:
        v1,v2,cost = int(i.split('-')[0]),int(i.split('-')[1].split(',')[0]),int(i.split('-')[1].split(',')[1])
        data.append([v1,v2,cost])
        max_n = max(v1,v2,max_n)
    graph = [[M for _ in range(max_n+1)] for _ in range(max_n+1)]
    for i in data:
        graph[i[0]][i[1]] = i[2]
    for i in range(len(graph)):
        graph[i][i] = 0
    return graph


def report_indegree_and_outdegree(graph,vertex):
    indegree = 0
    outdegree = 0
    for i in range(len(graph[vertex])):
        if graph[vertex][i] != 0 and graph[vertex][i] != M:
            outdegree += 1
    for i in range(len(graph)):
        if graph[i][vertex] != 0 and graph[i][vertex] != M:
            indegree += 1
    print(f'vertex:{vertex},indegree:{indegree},outdegree:{outdegree}')


def display_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            print('{:<8}'.format(graph[i][j]),end=' ')
        print()


def shortest_path(graph):
    vertex1 = int(input('Please enter vertex1:'))
    vertex2 = int(input('Please enter vertex2:'))
    n = len(graph)
    found = [vertex1]
    cost = [M] * n
    cost[vertex1] = 0
    path = [[]]*n
    path[vertex1] = [vertex1]
    while len(found) < n:
        min_value = M+1
        col = -1
        row = -1
        for f in found:
            for i in [x for x in range(n) if x not in found]:
                if graph[f][i] + cost[f] < min_value:
                    min_value = graph[f][i] + cost[f]
                    row = f
                    col = i
        if col == -1 or row == -1:
            break
        found.append(col)
        cost[col] = min_value
        path[col] = path[row][:]
        path[col].append(col)
    print(f'cost:{cost[vertex2]},path:{path[vertex2]}')


if __name__ == '__main__':
    graph = construct_graph('input_file')
    display_graph(graph)
    report_indegree_and_outdegree(graph,0)
    shortest_path(graph)

