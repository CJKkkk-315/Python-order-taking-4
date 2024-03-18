import csv
# 读取数据
data = []
with open('link1.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = data[1:]
nodes = set()
for i in data:
    nodes.add(i[1])
nodes = sorted(list(nodes))
# 定义图中的节点数量
num_nodes = len(nodes)
# 定义图中的边，以及边的权值。

# 在这里，我们使用一个二维数组表示图，其中graph[i][j]表示节点i到节点j的边的权值。
# 如果节点i和节点j之间没有边，那么graph[i][j]的值就是无穷大（float("inf")）。
graph = [[float("inf") for j in range(num_nodes)] for i in range(num_nodes)]

for i in data:
    graph[nodes.index(i[1])][nodes.index(i[2])] = int(i[3])
for i in range(len(graph)):
    graph[i][i] = 0


def floyd(graph):
    # 初始化距离矩阵和路径矩阵
    distance = [[float("inf") for j in range(len(graph))] for i in range(len(graph))]
    paths = [[0 for j in range(len(graph))] for i in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
                paths[i][j] = j
    # 开始Floyd算法
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    paths[i][j] = paths[i][k]
    return distance, paths


start = '勤敏楼'
end = '食堂'
distance, paths = floyd(graph)
start_id = nodes.index(start)
end_id = nodes.index(end)
short_distance = distance[start_id][end_id]
path = []
now = start_id
while True:
    path.append(nodes[now])
    now = paths[now][end_id]
    if now == end_id:
        path.append(nodes[now])
        break
print(path)
print(short_distance)


