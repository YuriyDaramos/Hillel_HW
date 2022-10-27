import unittest
from Les_6_Kravchenko.list_simplifier import simplify_list


class TestCensor(unittest.TestCase):

    def test_list_in_list(self):
        self.assertEqual(simplify_list([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_list_in_tuple(self):
        self.assertEqual(simplify_list((1, [2, 3], 4)), [1, 2, 3, 4])

    def test_tuple_in_list(self):
        self.assertEqual(simplify_list([1, (2, 3), 4]), [1, 2, 3, 4])

    def test_set_in_list(self):
        self.assertEqual(simplify_list([1, {2}, 3]), [1, 2, 3])

    def test_triple_nesting(self):
        self.assertEqual(simplify_list([1, [2, [[3, 4], 5]], 6]), [1, 2, 3, 4, 5, 6])