import linecache
import os
import numpy as np

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


def get_number_of_nodes(filepath, desired_line_number=1):
    """Get number of nodes, using linecache in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of nodes of input graph.
    """
    return int(linecache.getline(filepath, desired_line_number).strip())


def get_number_of_edges(filepath, desired_line_number=2):
    """Get number of edges, using linecache in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 2.

    Returns:
        int: the number of nodes of input graph.
    """
    return int(linecache.getline(filepath, desired_line_number).strip())


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


def opt_get_number_of_nodes(filepath, desired_line_number=1):
    """Get number of nodes, using loop for more optimized in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of nodes of input graph.
    """
    return int(getline(filepath, desired_line_number).strip())


def opt_get_number_of_edges(filepath, desired_line_number=2):
    """Get number of nodes, using loop for more optimized in the case of small files.

    Args:
        filepath (python.Str): Path to input file.
        desired_line_number (int, optional): desired line that need to be gotten. Defaults to 1.

    Returns:
        int: the number of edges of input graph.
    """
    return int(getline(filepath, desired_line_number).strip())


def get_adjacency_list(inp_vertex, data_path):
    data = getline(data_path, inp_vertex+2).strip().split(', ')
    adj_lst = []
    for item in data:
        vertex, data = item.split('(')
        label_edge, weight_edge = data[0:-1].split(',')
        adj_lst.append([int(vertex), int(label_edge), int(weight_edge)])
    return np.array(adj_lst)

def get_vertex_info(inp_vertex, datapath):
    data = getline(datapath, inp_vertex).strip()
    label, weight = data.split(':')[1][1:-1].split(',')
    return label, weight


def read_adjacency_list(filepath='adjacency_list.csv'):
    pass


def read_adjacency_matrix(filepath='adjacency_matrix.csv'):
    pass


def read_edge_list(filepath='edge_list.csv'):
    pass
