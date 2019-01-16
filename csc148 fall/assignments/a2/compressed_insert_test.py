import unittest
from prefix_tree import *


def repr_tree(t):
    if t.is_empty():
        return ''
    template = "Tree({} ({})"
    subtrees = ', '.join([repr_tree(s) for s in t.subtrees])
    if subtrees:
        subtrees = ' [' + subtrees + ']'
    return template.format(t.value, float(t.weight)) + subtrees + ')'


class TestInsert(unittest.TestCase):
    def test_insert_on_empty_tree(self):
        tree = CompressedPrefixTree('sum')
        tree.insert('Hello', 2.0, ['a', 'b'])
        expected = "Tree(['a', 'b'] (2.0) [Tree(Hello (2.0))])"
        self.assertEqual(expected, repr_tree(tree))

    def test_insert_fully_split_node(self):
        tree = CompressedPrefixTree('sum')
        tree.insert('Alice', 2.0, ['a', 'b'])
        tree.insert('Bob', 5.0, ['b', 'c'])
        expected = "Tree([] (7.0) [Tree(['b', 'c'] (5.0) [Tree(Bob (5.0))]), " \
                   "Tree(['a', 'b'] (2.0) [Tree(Alice (2.0))])])"
        self.assertEqual(expected, repr_tree(tree))

    def test_insert_partial_split_node(self):
        tree = CompressedPrefixTree('sum')
        tree.insert('Alice', 2.0, ['a', 'b'])
        tree.insert('Bob', 5.0, ['a', 'c'])
        expected = "Tree(['a'] (7.0) [Tree(['a', 'c'] (5.0) [Tree(Bob (5.0))]), " \
                   "Tree(['a', 'b'] (2.0) [Tree(Alice (2.0))])])"
        self.assertEqual(expected, repr_tree(tree))

    def test_all_common_prefix(self):
        tree = CompressedPrefixTree('sum')
        tree.insert('Alice', 4.0, ['a', 'b'])
        tree.insert('Bob', 3.0, ['a', 'b', 'c', 'd'])
        expected = "Tree(['a', 'b'] (7.0) [Tree(Alice (4.0)), Tree(['a', 'b', 'c', 'd'] (3.0) [Tree(Bob (3.0))])])"
        self.assertEqual(expected, repr_tree(tree))

    def test_create_common_prefix(self):
        tree = CompressedPrefixTree('sum')
        tree.insert('Alice', 100.0, ['f'])
        tree.insert('Bob', 3.0, ['a', 'b', 'c', 'd'])
        tree.insert('David', 4.0, ['a', 'b', 'c', 'f'])
        expected = "Tree([] (107.0) [Tree(['f'] (100.0) [Tree(Alice (100.0))]), Tree(['a', 'b', 'c'] (7.0) " \
                   "[Tree(['a', 'b', 'c', 'f'] (4.0) [Tree(David (4.0))]), Tree(['a', 'b', 'c', 'd'] (3.0) " \
                   "[Tree(Bob (3.0))])])])"
        self.assertEqual(expected, repr_tree(tree))

    def test_sample_on_handout(self):
        tree = CompressedPrefixTree('average')
        tree.insert('car', 100.0, ['c', 'a', 'r'])
        tree.insert('door', 4.0, ['d', 'o', 'o', 'r'])
        tree.insert('danger', 6.0, ['d', 'a', 'n', 'g', 'e', 'r'])
        tree.insert('cat', 20.0, ['c', 'a', 't'])
        tree.insert('care', 30.0, ['c', 'a', 'r', 'e'])
        expected = "Tree([] (32.0) [Tree(['c', 'a'] (50.0) [Tree(['c', 'a', 'r'] (65.0) [Tree(car (100.0))," \
                   " Tree(['c', 'a', 'r', 'e'] (30.0) [Tree(care (30.0))])]), Tree(['c', 'a', 't'] (20.0) " \
                   "[Tree(cat (20.0))])]), Tree(['d'] (5.0) [Tree(['d', 'a', 'n', 'g', 'e', 'r'] (6.0) " \
                   "[Tree(danger (6.0))]), Tree(['d', 'o', 'o', 'r'] (4.0) [Tree(door (4.0))])])])"
        self.assertEqual(expected, repr_tree(tree))







if __name__ == "__main__":
    unittest.main(exit=False)