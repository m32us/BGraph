from utils import listed_binary
from numpy import log2, floor

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

def preprocessing_graph(file_name='test_graph_00.csv'):
    fin = open('./data/' + file_name, "r")
    fout = open('./data/' + 'processed_' + file_name, 'w')
    num_nodes = fin.readline()
    print(floor(log2(int(num_nodes))))
    num_edges = fin.readline()
    # print(num_edges)
    fout.write(f"{num_nodes}")
    fout.write(f"{num_edges}")

    lst_binary = list(listed_binary(
        floor(log2(int(num_nodes))) + 1
        ))

    print(lst_binary)

    for count, line in enumerate(fin.readlines()):
        adj_vertex = line.split(', ')
        curr_vertex_boolean_formula = lst_binary[count]
        for adj in adj_vertex:
            vertex_boolean_formula = lst_binary[int(adj)]
            fout.write(f"{curr_vertex_boolean_formula+vertex_boolean_formula}\n")

    fin.close()
    fout.close()

preprocessing_graph()

