from unittest import TestCase

from bgraph.core import ABCEdge


class TestEdge(TestCase):
    def test_case_00(self):
        e12 = ABCEdge(label=12, data=69)
        assert isinstance(e12, ABCEdge)

    def test_case_01(self):
        e12 = ABCEdge(label=12, data=69)
        assert isinstance(e12, ABCEdge)
        assert e12.get_label() == 12

    def test_case_02(self):
        e12 = ABCEdge(label=12, data=69)
        assert isinstance(e12, ABCEdge)
        assert e12.get_label() == 12
        assert e12.get_data() == 69

