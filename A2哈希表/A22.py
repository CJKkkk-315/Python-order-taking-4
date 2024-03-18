import random
from collections import defaultdict, deque
import heapq

class Graph:
    def __init__(self, n):
        self.vertices = [i for i in range(n)]
        self.adj_list = defaultdict(list)
        for i in range(1,n):
            x = random.randint(0, i-1)
            S = random.sample([j for j in range(i-1)],x)
            for s in S:
                w = random.randint(10,100)
                self.adj_list[self.vertices[i]].append((self.vertices[s], w))
                self.adj_list[self.vertices[s]].append((self.vertices[i], w))

    def bfs_tree(self):
        visited = [False] * len(self.vertices)
        tree_edges = []
        queue = deque([self.vertices[0]])

        while queue:
            vertex = queue.popleft()
            visited[vertex] = True

            for neighbor, weight in self.adj_list[vertex]:
                if not visited[neighbor]:
                    tree_edges.append((vertex, neighbor, weight))
                    visited[neighbor] = True
                    queue.append(neighbor)

        return tree_edges

    def prim_tree(self):
        tree_edges = []
        visited = [False] * len(self.vertices)
        priority_queue = [(0, self.vertices[0], -1)]

        while priority_queue:
            weight, vertex, parent = heapq.heappop(priority_queue)
            if not visited[vertex]:
                visited[vertex] = True
                tree_edges.append((parent, vertex, weight))

                for neighbor, edge_weight in self.adj_list[vertex]:
                    if not visited[neighbor]:
                        heapq.heappush(priority_queue, (edge_weight, neighbor, vertex))

        return tree_edges[1:]


if __name__ == "__main__":
    k = 100
    for n in [20,40,60]:
        Diffs = []
        for times in range(k):
            random_graph = Graph(n)
            B = sum([i[2] for i in random_graph.bfs_tree()])
            P = sum([i[2] for i in random_graph.prim_tree()])
            Diff = (B-P)/P * 100
            Diffs.append(Diff)
        avg_Diff = round(sum(Diffs)/len(Diffs),2)
        print(f'n={n}:average Diff={avg_Diff}%')
