from unittest import TestCase

from bgraph.core import UDBGraph, ABCNode
from bgraph.utils import read_graph_from_file

class TestUDBGraph(TestCase):
    def test_case_00(self):
        g = UDBGraph()
        assert isinstance(g, UDBGraph)

    def test_case_01(self):
        # g = UDBGraph(data_path='gdata_undirected')
        g = read_graph_from_file('gdata_undirected')
        assert isinstance(g, UDBGraph)
        assert g.get_num_nodes() == 8
        assert g.get_num_edges() == 32

    def test_case_02(self):
        g = UDBGraph()
        v = ABCNode()
        g.add_node(v)
        assert isinstance(g, UDBGraph)
        assert g.get_num_nodes() == 1

    def test_case_03(self):
        g = UDBGraph()
        g.add_node(ABCNode(1))
        g.add_node(ABCNode(2))
        g.add_edge(1,2)
        assert g.num_edge == 1
        assert g.num_node == 2

    def test_case_04(self):
        g = UDBGraph()
        g.add_node(ABCNode(1))
        g.add_node(ABCNode(2))
        g.add_edge(1,2)
        g.add_edge(1,2)
        g.add_edge(1,2)
        assert g.num_edge == 3
        assert g.num_node == 2
        g.remove_edge(1,2,1)
        assert g.num_edge == 2
        assert g.num_node == 2
        g.remove_edge(1,2)

    def test_case_05(self):
        g = UDBGraph()
        g.add_node(ABCNode(1))
        g.add_node(ABCNode(2))
        g.remove_node(1)
        assert g.num_node == 1

    def run_test(self):
        self.test_case_00()
        self.test_case_01()
        self.test_case_02()
        self.test_case_03()
        self.test_case_04()
        self.test_case_05()

TestUDBGraph().run_test()
