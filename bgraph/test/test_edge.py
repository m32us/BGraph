from unittest import TestCase

from bgraph.core import ABCEdge


class TestEdge(TestCase):
    def test_case_00(self):
        e12 = ABCEdge(label=12, data=69)
        assert isinstance(e12, ABCEdge)

