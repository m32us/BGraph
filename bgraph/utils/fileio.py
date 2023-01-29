import linecache
import os
from typing import Optional, Tuple

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
        thefilepath (python.Str): Path to input file.
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


def opt_get_number_of_nodes(file_path, desired_line_number=1):
    """Get number of nodes, using loop for more optimized in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of nodes of input graph.
    """
    file_path += '/adj_lst'
    return int(getline(file_path, desired_line_number).strip())


def opt_get_number_of_edges(file_path, desired_line_number=2):
    """Get number of nodes, using loop for more optimized in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of edges of input graph.
    """
    file_path += '/adj_lst'
    return int(getline(file_path, desired_line_number).strip())


def get_adjacency_list(label: int, data_path: str):
    data_path += '/adj_lst'
    data = getline(data_path, label+2).strip().split(', ')

    # Danh sách nhãn đỉnh, trọng số cạnh, dữ liệu cạnh
    label_lst = []
    weight_edge_lst = []
    data_edge_lst = []

    for item in data:
        label_item, data_item = item.split('(')
        weight_edge, data_edge = data_item[0:-1].split(',')

        label_lst.append(label_item)
        weight_edge_lst.append(weight_edge)
        data_edge_lst.append(data_edge)

    return label_lst, weight_edge_lst, data_edge_lst

def get_node_info(label: int, data_path: str) -> tuple:
    """Get information of a node

    Args:
        label (int): Label of input node
        data_path (str): Path to database

    Returns:
        tuple: Tuple of vertex weight, vertex data
    """
    data_path += '/vertices_lst'

    # Đọc dòng có nhãn là label
    data = getline(data_path, label).strip()

    # Lấy ra thông tin về trọng số, dữ liệu của đỉnh
    weight_vertex, data_vertex = data.split(':')[1][1:-1].split(',')

    # Trả về thông tin cần
    return weight_vertex, data_vertex

def remove_node_from_file(label:int, data_path:str):
    """Remove a node labelled as `label` from datafile.

    Args:
        label (int): Label of a node that need to be removed.
        data_path (str): Path to database.
    """
    adj_lst_filename = data_path + '/adj_lst'
    vertices_lst_filename = data_path + '/vertices_lst'
    pass

def remove_edge_from_file(label:int, data_path:str):
    """Remove an edge labelled as `label` from datafile.

    Args:
        label (int) : Label of an edge that need to be removed.
        data_path (str): Path to database.
    """
    pass

def add_node_to_file(label:int, data: Optional[object], data_path: str):
    """Add a node labelled as `label`, store data as `data` [Optional] to datafile.

    Args:
        label (int): Label of a node that need to be added.
        data (Optional[object]): Data of this node.
        data_path (str): Path to database.
    """
    pass

def add_edge_to_file(label: int, data: Optional[object], data_path: str):
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
