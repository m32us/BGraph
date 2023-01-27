from unittest import TestCase

from bgraph.core import ABCEdge, ABCVertex


class TestEdge(TestCase):
    def test_case_00(self):
        v1 = ABCVertex(1, 'None')
        v2 = ABCVertex(2, 'Not None')
        e12 = ABCEdge(v1, v2, 'v12', 3)
        assert isinstance(e12, ABCEdge)

    def test_case_01(self):
        v1 = ABCVertex(1, 'None')
        v2 = ABCVertex(2, 'Not None')
        e12 = ABCEdge(v1, v2, 'v12', 3)
        assert isinstance(e12, ABCEdge)
        assert e12.get_from_vertex() == v1

    def test_case_02(self):
        v1 = ABCVertex(1, 'None')
        v2 = ABCVertex(2, 'Not None')
        e12 = ABCEdge(v1, v2, 'v12', 3)
        assert isinstance(e12, ABCEdge)
        assert e12.get_from_vertex() == v1
        assert e12.get_to_vertex() == v2

    def test_case_03(self):
        v1 = ABCVertex(1, 'None')
        v2 = ABCVertex(2, 'Not None')
        e12 = ABCEdge(v1, v2, 'v12', 3)
        assert isinstance(e12, ABCEdge)
        assert e12.get_from_vertex() == v1
        assert e12.get_to_vertex() == v2
        assert e12.get_label() == 'v12'