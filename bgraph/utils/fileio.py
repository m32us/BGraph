import linecache
import os
import errno
from typing import Optional, Tuple, List, Union
from bgraph.core import ABCGraph, ABCEdge, ABCNode, DEdge, DNode, DBGraph, UDBGraph

def read_tail(fname, lines):
    """Read last N lines from file fname."""
    f = open(fname, 'r')
    BUFSIZ = 1024
    f.seek(0, os.SEEK_END)
    fsize = f.tell()
    block = -1
    data = ""
    exit = False
    while not exit:
        step = (block * BUFSIZ)
        if abs(step) >= fsize:
            f.seek(0)
            exit = True
        else:
            f.seek(step, os.SEEK_END)
        data = f.read().strip()
        if data.count('\n') >= lines:
            break
        else:
            block -= 1
    return data.splitlines()[-lines:]


def buf_count_newlines_gen(fname):
    def _make_gen(reader):
        while True:
            b = reader(2 ** 16)
            if not b:
                break
            yield b

    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
    return count


def get_number_of_nodes(file_path, desired_line_number=1):
    """Get number of nodes, using linecache in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of nodes of input graph.
    """
    file_path += '/adj_lst'
    return int(linecache.getline(file_path, desired_line_number).strip())


def get_number_of_edges(file_path, desired_line_number=2):
    """Get number of edges, using linecache in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 2.

    Returns:
        int: the number of nodes of input graph.
    """
    file_path += '/adj_lst'
    return int(linecache.getline(file_path, desired_line_number).strip())


def getline(file_path, desired_line_number):
    """Get line using for loop

    Args:
        file_path (python.Str): Path to input file.
        desired_line_number (python.Integer): desired line that need to be gotten.

    Returns:
        str: string of desired line that need to be gotten.
    """
    if desired_line_number < 1:
        return ''
    current_line_number = 0
    for line in open(file_path):
        current_line_number += 1
        if current_line_number == desired_line_number:
            return line
    return ''


# def opt_get_number_of_nodes(file_path, desired_line_number=1):
#     """Get number of nodes, using loop for more optimized in the case of small files.

#     Args:
#         filepath (python.Str): Path to input file.
#         desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

#     Returns:
#         int: the number of nodes of input graph.
#     """
#     file_path += '/adj_lst'
#     return int(getline(file_path, desired_line_number).strip())


# def opt_get_number_of_edges(file_path, desired_line_number=2):
#     """Get number of nodes, using loop for more optimized in the case of small files.

#     Args:
#         filepath (python.Str): Path to input file.
#         desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

#     Returns:
#         int: the number of edges of input graph.
#     """
#     file_path += '/adj_lst'
#     return int(getline(file_path, desired_line_number).strip())


def get_adjacency_list(label: int, data_path: str) -> Tuple[List, List, List]:
    data_path += '/adj_lst'
    data = getline(data_path, label).strip().split(':')[1].split(',')

    # Danh sách nhãn đỉnh, trọng số cạnh, dữ liệu cạnh
    lst_label_nodes = []
    lst_label_edges = []
    lst_data_edges = []

    for item in data:
        data = data[:-1]
        label_adj_node, data_item = item.split('(')
        label_edge, data_edge = data_item.split('-')

        lst_label_nodes.append(label_adj_node)
        lst_label_edges.append(label_edge)
        lst_data_edges.append(data_edge)

    return lst_label_nodes, lst_label_edges, lst_data_edges


def get_node_info(label: int, data_path: str) -> Tuple[object, object]:
    """Get information of a node

    Args:
        label (int): Label of input node
        data_path (str): Path to database

    Returns:
        tuple: Tuple of node label, node data
    """
    data_path += '/vertices_lst'

    # Đọc dòng có nhãn là label
    inp_data = getline(data_path, label).strip()

    # Lấy ra thông tin về trọng số, dữ liệu của đỉnh
    label_node, data_node = inp_data.split(':')

    # Trả về thông tin cần
    return label_node, data_node


def save_graph(lst_nodes: dict, is_directed: bool, data_path: str = None):
    try:
        os.makedirs(data_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    adj_lst_filepath = data_path + '/adj_lst'
    vertices_lst_filepath = data_path + '/vertices_lst'

    with open(adj_lst_filepath, 'w') as alf, open(vertices_lst_filepath, 'w') as vlf:
        if is_directed:
            alf.write("D\n")
        else:
            alf.write("D\n")

        for key, value in lst_nodes.items():
            node_info = str(key) + ':' + str(value.get_label())
            alf.write(f"{node_info}\n")

            if not is_directed:
                adj_info = str(key) + ':'
                for x, y in zip(value.get_list_neighbor(), value.get_list_edge()):
                    adj_info += (str(x) + '(' + str(y.get_label()) +
                                 '-' + str(y.get_data()) + ')') + ','
                adj_info = adj_info[:-1]
                vlf.write(f"{adj_info}\n")
            else:
                pass

        alf.truncate(alf.tell()-1)
        vlf.truncate(vlf.tell()-1)

        alf.close()
        vlf.close()


def remove_node_from_file(del_label_node: int, modified_lst_nodes: dict, data_path: str):
    """Remove a node labelled as `label` from datafile.

    Args:
        label (int): Label of a node that need to be removed.
        data_path (str): Path to database.
    """
    # Khởi tạo địa chỉ cần đến
    adj_lst_filename = data_path + '/adj_lst'
    vertices_lst_filename = data_path + '/vertices_lst'

    BLOCK_SIZE = 1 << 15
    # Xử lý tập tin danh sách kề
    for line in open(adj_lst_filename):
        pass

    # Xử lý tập tin danh sách đỉnh


def remove_edge_from_file(del_label_edge: int, modified_lst_nodes: dict, data_path: str):
    """Remove an edge labelled as `label` from datafile.

    Args:
        label (int) : Label of an edge that need to be removed.
        data_path (str): Path to database.
    """
    pass


def __check_node_exist(node_label: int, data_path: str) -> bool:
    vertices_lst_filename = data_path + '/vertices_lst'
    for line in open(vertices_lst_filename):
        if line[0] == str(node_label):
            return True
    return False


def __check_edge_exist(start_node_label: Optional[int], end_node_label: Optional[int], edge_label: Optional[int], data_path: str, is_graph_directed: Optional[bool] = False) -> bool:
    if not __check_node_exist(start_node_label, data_path) or not __check_node_exist(end_node_label):
        return False
    adjn_start_node, lst_adje_start_node, _ = get_adjacency_list(
        start_node_label, data_path)
    adjn_end_node, lst_adje_end_node, _ = get_adjacency_list(
        end_node_label, data_path)
    if start_node_label is not None and end_node_label is not None:
        if is_graph_directed:
            if start_node_label in adjn_end_node or end_node_label in adjn_start_node:
                return True
            else:
                return False
        else:
            if start_node_label is not None and end_node_label is not None:
                return True
            else:
                return False
    else:
        if edge_label in lst_adje_start_node or edge_label in lst_adje_end_node:
            return True


def add_node_to_file(node_label: int, node_data: Optional[object], data_path: str):
    """Add a node labelled as `label`, store data as `data` [Optional] to datafile.

    Args:
        label (int): Label of a node that need to be added.
        data (Optional[object]): Data of this node.
        data_path (str): Path to database.
    """
    if not __check_node_exist(node_label=node_label, data_path=data_path):
        pass


def add_edge_to_file(start_node_label: int, end_node_label: int, data: Optional[object], data_path: str):
    """Add an edge labelled as `label`, store data as `data` [Optional] to data file

    Args:
        label (int): Label of an edge that need to be added.
        data (Optional[object]): Data of this edge.
        data_path (str): Path to database.
    """


def read_adjacency_list(filepath='adjacency_list.csv'):
    pass


def read_adjacency_matrix(filepath='adjacency_matrix.csv'):
    pass


def read_edge_list(filepath='edge_list.csv'):
    pass

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
