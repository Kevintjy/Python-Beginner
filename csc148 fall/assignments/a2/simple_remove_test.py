import unittest
from prefix_tree import SimplePrefixTree


def repr_tree(t):
    if t.is_empty():
        return ''
    template = "Tree({} ({})"
    subtrees = ', '.join([repr_tree(s) for s in t.subtrees])
    if subtrees:
        subtrees = ' [' + subtrees + ']'
    return template.format(t.value, float(t.weight)) + subtrees + ')'


class SimpleAutoCompleteTest(unittest.TestCase):

    def setUp(self):
        self.sum_tree = SimplePrefixTree('sum')
        self.avg_tree = SimplePrefixTree('average')

    def test_empty_tree_remove_no_prefix(self):
        self.sum_tree.remove([])
        expected = ""
        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_empty_tree_remove_extra_prefix(self):
        self.sum_tree.remove(['a'])
        expected = ""
        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_remove_leaf(self):
        self.sum_tree.insert('Bob', 6, [])
        self.sum_tree.insert('Alice', 5, [])
        self.sum_tree.remove([])
        print(repr_tree(self.sum_tree))
        expected = ""
        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_remove_update_weight(self):
        self.sum_tree.insert('Bob', 6, ['a', 'b'])
        self.sum_tree.insert('Alice', 5, ['a', 'c'])
        self.sum_tree.remove(['a', 'b'])
        expected = "Tree([] (5.0) [Tree(['a'] (5.0) [Tree(['a', 'c'] (5.0) [Tree(Alice (5.0))])])])"
        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_remove_update_avg(self):
        self.avg_tree.insert('Bob', 6, ['a', 'b'])
        self.avg_tree.insert('Alice', 4, ['a', 'c'])
        self.avg_tree.remove(['a', 'b'])
        expected = "Tree([] (4.0) [Tree(['a'] (4.0) [Tree(['a', 'c'] (4.0) [Tree(Alice (4.0))])])])"
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_remove_entire_subtree(self):
        self.avg_tree.insert('Bob', 6, ['a', 'b'])
        self.avg_tree.insert('Alice', 4, ['a', 'c'])
        self.avg_tree.insert('Jacky', 4, ['b', 'c'])
        self.avg_tree.remove(['a'])
        expected = "Tree([] (4.0) [Tree(['b'] (4.0) [Tree(['b', 'c'] (4.0) [Tree(Jacky (4.0))])])])"
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_remove_delete_empty_subtree(self):
        self.avg_tree.insert('Alice', 6, ['a'])
        self.avg_tree.insert('Bob', 6, ['a', 'b', 'c', 'd', 'e'])
        self.avg_tree.remove(['a', 'b', 'c', 'd', 'e'])
        expected = "Tree([] (6.0) [Tree(['a'] (6.0) [Tree(Alice (6.0))])])"
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_remove_non_exist_prefix(self):
        self.avg_tree.insert('Alice', 6, ['a'])
        self.avg_tree.insert('Bob', 6, ['a', 'b'])
        self.avg_tree.remove(['b'])
        expected = "Tree([] (6.0) [Tree(['a'] (6.0) [Tree(Alice (6.0)), Tree(['a', 'b'] (6.0) [Tree(Bob (6.0))])])])"
        self.assertEqual(repr_tree(self.avg_tree), expected)

if __name__ == '__main__':
    unittest.main()
