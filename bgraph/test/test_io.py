from unittest import TestCase

import numpy as np



# class TestIO(TestCase):
#     def test_case_00(self):
#         no_nodes = get_number_of_nodes('gdata_undirected')
#         assert no_nodes == 16

#     def test_case_02(self):
#         no_nodes = opt_get_number_of_nodes('gdata_undirected')
#         assert no_nodes == 16

#     def test_case_03(self):
#         no_nodes = get_number_of_edges('gdata_undirected')
#         assert no_nodes == 77

#     def test_case_04(self):
#         no_nodes = opt_get_number_of_edges('gdata_undirected')
#         assert no_nodes == 77

#     def test_case_05(self):
#         label, weight = get_node_info(5, 'gdata_undirected')
#         assert label == '17'
#         assert weight == '249'

    # def test_case_06(self):
    #     adj_lst = get_adjacency_list(1, 'gdata_undirected')
    #     assert adj_lst == (np.array([[1, 114, 991],
    #                                 [3, 114, 991],
    #                                 [4, 114, 991],
    #                                 [6, 114, 991],
    #                                 [7, 114, 991],
    #                                 [8, 114, 991],
    #                                 [12, 114, 991],
    #                                 [14, 114, 991],
    #                                 [15, 114, 991]]))
