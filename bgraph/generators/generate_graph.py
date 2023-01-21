from random import random
from itertools import product, combinations

def random_graph(n, p, *, directed=False, saved=False, filepath='test_graph_0.csv'):
    """random_graph

    Args:
        n (int): Initialise a graph with n nodes and no edges
        p (float/ double): threshold for determine whether add an edge
        directed (bool, optional): Determine whether graph is directed or undirected. Defaults to False.

    Algorithm:
        For each (unordered/ordered) pair of nodes (u, v):
            - Generate a random real number in the range [0, 1].
            - If this number is less than p, add edge (u - v) to graph

    Returns:
        list : adjacency list of graph
    """
    nodes = range(n)
    edges = 0
    adj_list = [[] for i in nodes]
    possible_edges = product(
        nodes, repeat=2) if directed else combinations(nodes, 2)
    for u, v in possible_edges:
        if random() < p:
            adj_list[u].append(v)
            if not directed:
                adj_list[v].append(u)
            edges += 1

    if saved and filepath is not None:
        with open(filepath, 'w') as f:
            f.write(f"{n}\n")
            f.write(f"{edges}\n")
            for line in adj:
                s = ', '.join(str(x) for x in line)
                f.write(f"{s}\n")

    return adj_list, n, edges


# TEST
adj, n, edges = random_graph(16, 0.6, directed=True)

