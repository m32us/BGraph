from pyeda.inter import *
import pydot
from graphviz import Source
import pandas as pd
import copy

# đọc num_edge dòng từ file input vào ram
def read_edge_from_file(filename:str, num_edge:int):
    Rs = []
    with open(filename) as fin:
        num_nodes = fin.readline()
        num_edges = fin.readline()
        for i in range(num_edge):
            line = fin.readline()
            if line != '':
                tmp = line.rstrip('\n')
                Rs.append([int(e) for e in tmp])
            else:
                break

    return pd.DataFrame(Rs)

def build_graph_from_file(filename:str):
    pass

def read_edge_list_from_file(filename:str):
    R = []
    with open(filename) as fin:
        num_nodes = fin.readline()
        num_edges = fin.readline()
        line = fin.readline() # phải đọc từng dòng vì bộ nhớ có hạn
        while line != '':
            R.append(line.rstrip('\n'))
            line = fin.readline()

    Rs = []
    for s in R:
        Rs.append([int(e) for e in s])

    return pd.DataFrame(Rs)

# for testing
def read_edge_list():
    R = ['000010','010000','100000','011000','110100','100001','010001','001011','101001','101111','111110','111011','110011']
    Rs = []
    for s in R:
        Rs.append([int(e) for e in s])
    return pd.DataFrame(Rs)

# D is a list of node (ascending order)
# s is pair generated from D
def gen_pair(i:int, s:list[int], D:list[int], list_pair:list[list[int]]):
    if i == len(s):
        if len(set(s)) == len(s):
            list_pair.append(s)
            print(s)
    else:
        for item in D:
            s[i] = item
            gen_pair(i+1, s, D, list_pair)

def convert_row_to_formula(row):
    row_formula = ['~'*abs(row[i]-1) + f'x{i}' for i in range(len(row))]
    return ' & '.join(row_formula)

def convert_bin_formula(R:pd.DataFrame):
    r_formulas = set()
    for row in R.iterrows():
        r_formula = convert_row_to_formula(row[1])
        r_formulas.add(r_formula)
    return r_formulas

def dec_to_bin(num:int, length=5):
    tmp = bin(num)[2:]
    return [int(i) for i in '0'*(length-len(tmp)) + tmp]

def check(s:list[int]):
    return len(set(s)) == len(s)

def gen_pair(i:int, pair:list[int], D:list[int], list_pair:list[list[int]]):
    if i == len(pair):
        if check(pair):
            list_pair.append(copy.deepcopy(pair))
    else:
        for item in D:
            pair[i] = item
            gen_pair(i+1, pair, D, list_pair)

def find_subgraph(list_node:list[int], expression:str):
    list_pair = []
    list_connection = []
    gen_pair(0, [0,0], list_node, list_pair)
    for connection in list_pair:
        str_formula = convert_row_to_formula(dec_to_bin(connection[0]) + dec_to_bin(connection[1]))
        if str_formula in expression:
            print(f'{connection}: {str_formula}')
            list_connection.append(str_formula)
    return list_connection

if __name__=='__main__':
    R = read_edge_list_from_file('./data/processed_test_graph_0.csv')
    # R = read_edge_from_file('./data/processed_test_graph_0.csv', 1000)
    expression = convert_bin_formula(R)
    # print(expression)
    # str_formula = convert_row_to_formula(dec_to_bin(2) + dec_to_bin(4))
    sub_graph = find_subgraph([0,2,4], expression)
