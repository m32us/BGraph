from typing import Optional, Union
from bgraph.core import ABCGraph, ABCEdge, ABCNode, DEdge, DNode, DBGraph, UDBGraph
import os

def parse_node(line:str):
    line = line.strip()
    elements = line.split(':')
    node_label = int(elements[0])
    node_data = elements[1]
    return ABCNode(node_label, node_data)

def parse_adj_list(line:str, is_directed:bool):
    line = line.strip()
    elements = line.split(':')
    node_label = int(elements[0])
    edges = elements[1].split(',')
    list_edge:list[ABCEdge] = []
    list_neighbor:list[int] = []
    for edge in edges:
        tmp = edge.split('(')
        if tmp[0] == '':
            break
        list_neighbor.append(int(tmp[0]))

        edge_label = int(tmp[1].split('-')[0])
        edge_data = tmp[1].split('-')[1][:-1]
        if is_directed:
            list_edge.append(DEdge('out', edge_label, edge_data))
        else:
            list_edge.append(ABCEdge(edge_label, edge_data))
    return node_label, list_neighbor, list_edge

def read_graph_from_file(data_path:str) -> Union[DBGraph, UDBGraph, FileNotFoundError, None]:
    node_file = os.path.join(data_path, 'vertices_lst')
    adj_list_file = os.path.join(data_path, 'adj_lst')
    graph:Optional[ABCGraph] = None
    try:
        with open(node_file, 'r') as fin:
            line = fin.readline().strip()
            if line == 'D':
                graph = DBGraph()
            elif line == 'U':
                graph = UDBGraph()
            else:
                raise KeyError('Notation of graph not in \{D, U\}')

            while True:
                line = fin.readline()
                if line == '':
                    break
                if line == '\n':
                    continue
                graph.add_node(parse_node(line))
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t load graph from {node_file}')

    try:
        with open(adj_list_file, 'r') as fin:
            while True:
                line = fin.readline()
                if line == '':
                    break
                if line == '\n':
                    continue
                node_label, list_neighbor, list_edge = parse_adj_list(line, graph.is_directed)
                for idx, neighbor in enumerate(list_neighbor):
                    graph.add_edge(node_label, neighbor, list_edge[idx])

    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t load edge from {adj_list_file}')

    return graph

graph = read_graph_from_file('./z')
graph.print_adj_list()

"""
# hàm đọc đồ thị từ file (đọc nguyên cái file)
# viết tại `./bgraph/core/` cho đồ thị có hướng (vô hướng đã viết bởi nam)
    - input là filename, output là object đồ thị
    - check kích thước của file
    - khởi tạo 1 đồ thị ABCGraph
    - viết hàm đọc 1node của đồ thị `read_node_from_file(filename, line_number)->ABCNode`. sau khi đọc xong node nghĩa là đã có danh sách kề các thứ rồi.
    - Add con node vừa đọc được vào đồ thị vừa khởi tạo

# hàm trích đồ thị con từ file (đọc các dòng xác đinh trong file)
# viết tại `./bgraph/algorithms`
    - input là filename, list_node:list[int] các label node cần rút trích, output là object đồ thị
    - nếu đọc tới dòng nào mà k có data thì raise lỗi
    - tạo con đồ thị
    - đọc dòng tới đâu trả ra node để add vào đồ thị tới đó. lúc vừa lấy được con node (gọi hàm `read_node_from_file`) thì chỉnh sửa lại danh sách kề và danh sách cạnh của node đó rồi thêm vào đồ thị
"""
