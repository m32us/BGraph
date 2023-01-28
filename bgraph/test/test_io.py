from unittest import TestCase

import numpy as np

from bgraph.utils import get_number_of_nodes, opt_get_number_of_nodes, \
get_number_of_edges, opt_get_number_of_edges, get_vertex_info, \
    get_adjacency_list

class TestIO(TestCase):
    def test_case_00(self):
        no_nodes = get_number_of_nodes('gdata_undirected/adj_lst')
        assert no_nodes == 16

    def test_case_02(self):
        no_nodes = opt_get_number_of_nodes('gdata_undirected/adj_lst')
        assert no_nodes == 16

    def test_case_03(self):
        no_nodes = get_number_of_edges('gdata_undirected/adj_lst')
        assert no_nodes == 73

    def test_case_04(self):
        no_nodes = opt_get_number_of_edges('gdata_undirected/adj_lst')
        assert no_nodes == 73

    def test_case_05(self):
        label, weight = get_vertex_info(5, 'gdata_undirected/vertices_lst')
        assert label == '8'
        assert weight == '48'

    def test_case_06(self):
        adj_lst = get_adjacency_list(1, 'gdata_undirected/adj_lst')
        assert adj_lst == np.array([[   2,    2, 1305],
                                    [   3,    2, 1305],
                                    [   6,    2, 1305],
                                    [   7,    2, 1305],
                                    [   8,    2, 1305],
                                    [  11,    2, 1305],
                                    [  13,    2, 1305],
                                    [  15,    2, 1305],])