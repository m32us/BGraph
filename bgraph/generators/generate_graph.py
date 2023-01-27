import os, errno
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
            for line in adj_list:
                s = ', '.join(str(x) for x in line)
                f.write(f"{s}\n")

    return adj_list, n, edges


# # TEST
# adj, n, edges = random_graph(16, 0.6, directed=True)


def random_graph_v2(n, p, *, directed=False, saved=True, folder_path='gdata'):
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

    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if saved:
        with open(os.path.join(folder_path + '/' + 'adj_lst'), 'w') as f:
            f.write(f"{n}\n")
            f.write(f"{edges}\n")
            for line in adj_list:
                label = round(random() * edges, 5)
                weight = int(random() * edges)
                s = ', '.join(str(x) + '(' + str(label) + ',' + str(weight) +')' for x in line)
                f.write(f"{s}\n")
            f.close()

        with open(os.path.join(folder_path + '/' + 'vertices_lst'), 'w') as f:
            for i in range(n):
                label = round(random() * n, 5)
                weight = int(random() * n)
                s = str(i) + ':' + '(' + str(label) + ',' + str(weight) +')'
                f.write(f"{s}\n")
            f.close()

    return adj_list, n, edges

