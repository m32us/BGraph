from unittest import TestCase

from bgraph.core import ABCVertex


class TestVertex(TestCase):
    def test_case_00(self):
        v1 = ABCVertex(1, 'None')
        assert isinstance(v1, ABCVertex)
        assert v1.get_label() is 'None'

    def test_case_01(self):
        v1 = ABCVertex(1)
        assert v1.get_label() is None
        assert isinstance(v1, ABCVertex)

    def test_case_02(self):
        v1 = ABCVertex(1, 'None')

        assert isinstance(v1, ABCVertex)
        assert v1.get_label() is 'None'

        v1.add_adjacency_vertex(2, 'food', 3)

        assert v1.get_adjacency_lst() == {(2, 'food')}

    def test_case_03(self):
        v1 = ABCVertex(1, 'None')

        assert isinstance(v1, ABCVertex)
        assert v1.get_label() is 'None'

        v1.add_adjacency_vertex(2, 'food', 3)
        assert v1.get_adjacency_lst() == {(2, 'food')}
        assert v1.get_vertex_weight(2) == 3
