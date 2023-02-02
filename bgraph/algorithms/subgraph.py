import os
import linecache
from bgraph.core import DBGraph, UDBGraph, ABCGraph
from bgraph.utils.fileio import parse_adj_list, parse_node
from typing import Optional


def load_subgraph(list_label:list[int], data_path:str):
    """Mô tả: Rút trích đồ thị con dựa trên một danh sách node cho trước

    Args:
        list_label (list[int]): danh sách nhãn của các node
        data_path (str): đường dẫn đến file dữ liệu đồ thị (sẽ nói kỹ ở phần Cấu trúc tệp tin)

    Raises:
        FileNotFoundError: Raise nếu file dữ liệu đồ thị không tồn tại
        KeyError: Raise nếu cấu trúc file bị sai định dạng

    Returns:
        [UDBGraph, DBGraph]: Trả về đối tượng đồ thị có hướng hoặc vô hướng
    """
    sub_graph:Optional[ABCGraph] = None
    node_file = os.path.join(data_path, 'vertices_lst')
    adj_list_file = os.path.join(data_path, 'adj_lst')

    try:
        type_graph = linecache.getline(node_file, 1).strip()
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t load node of graph from {node_file}')

    if type_graph == 'D':
        sub_graph = DBGraph()
    elif type_graph == 'U':
        sub_graph = UDBGraph()
    else:
        raise KeyError('Notation of graph not in \{D, U\}')

    current_line_number = 0
    for line_node in open(node_file):
        current_line_number += 1
        if current_line_number == 1:
            continue
        if line_node == '':
            break
        if line_node == '\n':
            continue
        if current_line_number-2 in list_label: #count node from 0
            sub_graph.add_node(parse_node(line_node))

    try:
        current_line_number = 0
        for line in open(adj_list_file):
            current_line_number += 1
            if line == '':
                break
            if line == '\n':
                continue
            if current_line_number-1 in list_label: #count node from 0
                node_label, list_neighbor, list_edge = parse_adj_list(line, sub_graph.is_directed)
                for idx, neighbor in enumerate(list_neighbor):
                    # nếu node không tồn tại trong list_node nhưng tồn tại trong list_edge (node bên kia k nằm trong subgraph)
                    try:
                        sub_graph.add_edge(node_label, neighbor, list_edge[idx])
                    except KeyError:
                        pass
    except FileNotFoundError:
        raise FileNotFoundError(f'Can\'t load edge from {adj_list_file}')

    print(f'Loaded {list_label} from {data_path}')
    return sub_graph

