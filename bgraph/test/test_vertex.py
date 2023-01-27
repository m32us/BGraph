from unittest import TestCase

from bgraph.core import ABCVertex

class TestVertex(TestCase):
    def test_case_00(self):
        v1 = ABCVertex(1, 'None')
        assert isinstance(v1, ABCVertex)
        assert v1.get_label() is 'None'

    def test_case_00(self):
        v1 = ABCVertex(1)
        assert v1.get_label() is None
        assert isinstance(v1, ABCVertex)