from unittest import TestCase

from bgraph.core import UDBGraph, ABCNode

class TestUDBGraph(TestCase):
    def test_case_00(self):
        g = UDBGraph()
        assert isinstance(g, UDBGraph)

    def test_case_01(self):
        g = UDBGraph(data_path='gdata_undirected')
        assert isinstance(g, UDBGraph)
        assert g.get_num_nodes() == 16
        assert g.get_num_edges() == 77

    def test_case_00(self):
        g = UDBGraph()
        v = ABCNode()
        g.add_node(v)
        assert isinstance(g, UDBGraph)
        assert g.get_num_nodes() == 1

