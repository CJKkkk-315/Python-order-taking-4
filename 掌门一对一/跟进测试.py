import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, value1, value2):
        self.val = f'{value1},{value2}'
        self.left = None
        self.right = None
        self.id = id(self)  # Unique identifier for the node


def add_nodes_edges_improved(tree, graph, parent=None, pos={}, x=0, y=0, layer=1, width_factor=1.5):
    if tree is not None:
        graph.add_node(tree.id, label=tree.val)
        pos[tree.id] = (x, y)
        if parent is not None:
            graph.add_edge(parent.id, tree.id)

        # Increase horizontal space with each additional layer
        horizontal_gap = width_factor ** layer
        add_nodes_edges_improved(tree.left, graph, tree, x=x-horizontal_gap, y=y-1, pos=pos, layer=layer+1, width_factor=width_factor)
        add_nodes_edges_improved(tree.right, graph, tree, x=x+horizontal_gap, y=y-1, pos=pos, layer=layer+1, width_factor=width_factor)
    return pos

tree = TreeNode(0,0)
def count_partition(n, m, tree, is_left):
    if is_left:
        tree.left = TreeNode(n,m)
        tree = tree.left
    else:
        tree.right = TreeNode(n,m)
        tree = tree.right
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    return count_partition(n - m, m, tree, True) + count_partition(n, m - 1, tree, False)
count_partition(5,3,tree,True)

graph_improved = nx.DiGraph()
pos_improved = add_nodes_edges_improved(tree.left, graph_improved)

# Draw the graph with improved spacing
plt.figure(figsize=(10, 8))
nx.draw(graph_improved, pos_improved, labels=nx.get_node_attributes(graph_improved, 'label'), with_labels=True, arrows=False)
plt.title('Improved Binary Tree Visualization')
plt.show()
