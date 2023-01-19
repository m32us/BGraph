from utils import listed_binary

# def read_edgelist(file_path='data/input_9.csv'):
#     num_nodes = 64
#     nodes = range(num_nodes)
#     adj_list = [[] for i in nodes]
#     with open(file_path, 'r') as f:
#        for count, line in enumerate(f):
#            u, v = line.split(' ')
#            u, v = int(u), int(v)
#            if adj_list[u] is None or v not in adj_list[u]:
#                adj_list[u].append(v)
#     return adj_list, num_nodes, count + 1

# adj_list, num_nodes, count = read_edgelist()

# with open('test_graph_9.csv', 'w') as f:
#     f.write(f"{num_nodes}\n")
#     f.write(f"{count}\n")
#     for line in adj_list:
#         s = ', '.join(str(x) for x in line)
#         f.write(f"{s}\n")

def preprocessing_graph(file_path='./test_graph.csv'):
    pass


