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


class SimpleInsertTest(unittest.TestCase):

    def setUp(self):
        self.sum_tree = SimplePrefixTree('sum')
        self.avg_tree = SimplePrefixTree('average')

    def test_insert_leaf(self):
        self.sum_tree.insert('Gary', 5, [])
        self.avg_tree.insert('Gary', 5, [])

        expected = "Tree([] (5.0) [Tree(Gary (5.0))])"

        self.assertEqual(repr_tree(self.sum_tree), expected)
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_update_leaf_weight(self):
        self.sum_tree.insert('Gary', 5, [])
        self.sum_tree.insert('Gary', 5, [])

        self.avg_tree.insert('Gary', 5, [])
        self.avg_tree.insert('Gary', 5, [])

        expected = "Tree([] (10.0) [Tree(Gary (10.0))])"

        self.assertEqual(repr_tree(self.sum_tree), expected)
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_insert_create_internal(self):
        expected = "Tree([] (5.0) [Tree(['a'] (5.0) [Tree(Gary (5.0))])])"

        self.sum_tree.insert('Gary', 5, ['a'])
        self.assertEqual(repr_tree(self.sum_tree), expected)

        self.avg_tree.insert('Gary', 5, ['a'])
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_insert_multi_internals(self):
        self.sum_tree.insert('Gary', 5, ['a', 'b', 'c'])
        self.avg_tree.insert('Gary', 5, ['a', 'b', 'c'])

        expected = "Tree([] (5.0) [Tree(['a'] (5.0) [Tree(['a', 'b'] (5.0) " \
                   "[Tree(['a', 'b', 'c'] (5.0) [Tree(Gary (5.0))])])])])"

        self.assertEqual(repr_tree(self.sum_tree), expected)
        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_insert_sum_tree_two_branches(self):
        self.sum_tree.insert('ac', 4, ['a', 'c'])
        self.sum_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (10.0) [Tree(['a'] (10.0) [Tree(['a', 'b'] (6.0) " \
                   "[Tree(ab (6.0))]), Tree(['a', 'c'] (4.0) [Tree(ac (4.0))])])])"

        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_insert_avg_tree_two_branches(self):
        self.avg_tree.insert('ac', 4, ['a', 'c'])
        self.avg_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (5.0) [Tree(['a'] (5.0) [Tree(['a', 'b'] (6.0) " \
                   "[Tree(ab (6.0))]), Tree(['a', 'c'] (4.0) [Tree(ac (4.0))])])])"

        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_sum_tree_contains_leave_and_subtree(self):
        self.sum_tree.insert('a', 4, ['a'])
        self.sum_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (10.0) [Tree(['a'] (10.0) [Tree(['a', 'b'] (6.0) [Tree(ab (6.0))]), Tree(a (4.0))])])"

        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_avg_tree_contains_leave_and_subtree(self):
        self.avg_tree.insert('a', 4, ['a'])
        self.avg_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (5.0) [Tree(['a'] (5.0) [Tree(['a', 'b'] (6.0) [Tree(ab (6.0))]), Tree(a (4.0))])])"

        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_sum_tree_insert_dup(self):
        self.sum_tree.insert('ab', 6, ['a', 'b'])
        self.sum_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (12.0) [Tree(['a'] (12.0) [Tree(['a', 'b'] (12.0) [Tree(ab (12.0))])])])"

        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_avg_tree_insert_dup(self):
        self.avg_tree.insert('ab', 6, ['a', 'b'])
        self.avg_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (12.0) [Tree(['a'] (12.0) [Tree(['a', 'b'] (12.0) [Tree(ab (12.0))])])])"

        self.assertEqual(repr_tree(self.avg_tree), expected)

    def test_sum_tree_insert_dup_change_order(self):
        self.sum_tree.insert('ab', 4, ['a', 'b'])
        self.sum_tree.insert('ac', 6, ['a', 'c'])
        self.sum_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (16.0) [Tree(['a'] (16.0) [Tree(['a', 'b'] (10.0) " \
                   "[Tree(ab (10.0))]), Tree(['a', 'c'] (6.0) [Tree(ac (6.0))])])])"

        self.assertEqual(repr_tree(self.sum_tree), expected)

    def test_avg_tree_insert_dup_change_order(self):
        self.avg_tree.insert('ab', 4, ['a', 'b'])
        self.avg_tree.insert('ac', 6, ['a', 'c'])
        self.avg_tree.insert('ab', 6, ['a', 'b'])

        expected = "Tree([] (8.0) [Tree(['a'] (8.0) [Tree(['a', 'b'] (10.0) " \
                   "[Tree(ab (10.0))]), Tree(['a', 'c'] (6.0) [Tree(ac (6.0))])])])"

        self.assertEqual(repr_tree(self.avg_tree), expected)








if __name__ == '__main__':
    unittest.main()
