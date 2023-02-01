from unittest import TestCase

from bgraph.core import DBGraph, DNode, ABCNode
from bgraph.utils import read_graph_from_file

class TestDBGraph(TestCase):
    def test_case_00(self):
        g = DBGraph()
        assert isinstance(g, DBGraph)

    def test_case_01(self):
        g = read_graph_from_file('gdata_directed')
        assert isinstance(g, DBGraph)
        assert g.num_node == 8
        assert g.num_edge == 38

    def test_case_02(self):
        g = DBGraph()
        v = DNode()
        g.add_node(v)
        assert isinstance(g, DBGraph)
        assert g.num_node == 1

    def test_case_03(self):
        g = DBGraph()
        g.add_node(ABCNode(1))
        g.add_node(ABCNode(2))
        g.add_edge(1,2)
        assert g.num_edge == 1
        assert g.num_node == 2

    def test_case_04(self):
        g = DBGraph()
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
        g = DBGraph()
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

TestDBGraph().run_test()
