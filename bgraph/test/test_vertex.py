from unittest import TestCase

from bgraph.core import ABCNode


class TestVertex(TestCase):
    def test_case_00(self):
        v1 = ABCNode(label=1, data=69)
        assert isinstance(v1, ABCNode)
        assert v1.get_label() == 1

    def test_case_01(self):
        v1 = ABCNode(label=1)
        assert isinstance(v1, ABCNode)
        assert v1.get_label() == 1

    def test_case_02(self):
        v1 = ABCNode(label=1, data=69)
        assert isinstance(v1, ABCNode)
        assert v1.get_label() == 1
        assert v1.get_data() == 69



