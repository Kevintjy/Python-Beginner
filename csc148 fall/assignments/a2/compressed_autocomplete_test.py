import unittest
from prefix_tree import CompressedPrefixTree


def repr_tree(t):
    if t.is_empty():
        return ''
    template = "Tree({} ({})"
    subtrees = ', '.join([repr_tree(s) for s in t.subtrees])
    if subtrees:
        subtrees = ' [' + subtrees + ']'
    return template.format(t.value, float(t.weight)) + subtrees + ')'


class CompressedAutoCompleteTest(unittest.TestCase):

    def setUp(self):
        self.sum_tree = CompressedPrefixTree('sum')

    def test_empty_tree_no_prefix(self):
        self.assertEqual(self.sum_tree.autocomplete([]), [])

    def test_empty_tree_extra_prefix(self):
        self.assertEqual(self.sum_tree.autocomplete(['c']), [])

    def test_one_leaf_no_prefix(self):
        self.sum_tree.insert('Alice', 5, [])
        expected = [('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete([]), expected)

    def test_one_leaf_no_prefix_zero_limit(self):
        self.sum_tree.insert('Alice', 5, ['a'])
        self.assertEqual(self.sum_tree.autocomplete(['a'], 0), [])

    def test_one_leaf_no_prefix_at_limit(self):
        self.sum_tree.insert('Alice', 5, [])
        expected = [('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete([], 1), expected)

    def test_multi_leaf_no_prefix_extra_limit(self):
        self.sum_tree.insert('Alice', 5, [])
        self.sum_tree.insert('Jacky', 11, [])
        self.sum_tree.insert('Bob', 10, [])
        expected = [('Jacky', 11.0), ('Bob', 10.0), ('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete([], 4), expected)

    def test_multi_leaf_no_prefix_not_enough_limit(self):
        self.sum_tree.insert('Alice', 5, [])
        self.sum_tree.insert('Jacky', 11, [])
        self.sum_tree.insert('Bob', 10, [])
        expected = [('Jacky', 11.0), ('Bob', 10.0)]
        self.assertEqual(self.sum_tree.autocomplete([], 2), expected)

    def test_multi_internal_no_prefix(self):
        self.sum_tree.insert('Alice', 5, ['a'])
        self.sum_tree.insert('Jacky', 11, ['a', 'c'])
        self.sum_tree.insert('Bob', 10, ['b'])
        expected = [('Jacky', 11.0), ('Bob', 10.0), ('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete([], 3), expected)

    def test_with_multi_internal_and_prefix(self):
        self.sum_tree.insert('Alice', 5, ['a'])
        self.sum_tree.insert('Jacky', 11, ['a'])
        self.sum_tree.insert('Bob', 10, ['b'])
        expected = [('Jacky', 11.0), ('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete(['a'], 3), expected)

    def test_multi_internal_extra_prefix(self):
        self.sum_tree.insert('Alice', 5, ['a'])
        self.sum_tree.insert('Jacky', 11, ['a'])
        self.sum_tree.insert('Bob', 10, ['b'])
        expected = []
        self.assertEqual(self.sum_tree.autocomplete(['a', 'b'], 3), expected)

    def test_multi_internal_short_prefix(self):
        self.sum_tree.insert('Alice', 5, ['a', 'b'])
        self.sum_tree.insert('Jacky', 11, ['a', 'c'])
        self.sum_tree.insert('Bob', 10, ['b'])
        expected = [('Jacky', 11.0), ('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete(['a'], 3), expected)

    def test_multi_level_leaves(self):
        self.sum_tree.insert('Alice', 5, ['a'])
        self.sum_tree.insert('Jacky', 11, ['a', 'c'])
        self.sum_tree.insert('Bob', 10, ['b'])
        expected = [('Jacky', 11.0), ('Alice', 5.0)]
        self.assertEqual(self.sum_tree.autocomplete(['a'], 3), expected)

    def test_multi_internal_limit_cutoff(self):
        self.sum_tree.insert('Alice', 5, ['a', 'c'])
        self.sum_tree.insert('Jacky', 11, ['a', 'c'])
        expected = [('Jacky', 11.0)]
        self.assertEqual(self.sum_tree.autocomplete(['a'], 1), expected)

    def test_multi_internal_limit_continue(self):
        self.sum_tree.insert('Alice', 5, ['a', 'c', 'b', 'b'])
        self.sum_tree.insert('Jacky', 10, ['a', 'c', 'b', 'f'])
        self.sum_tree.insert('Bob', 11, ['a', 'd'])
        self.sum_tree.insert('Kevin', 9, ['a', 'd'])
        expected = [('Bob', 11.0), ('Jacky', 10.0), ('Kevin', 9.0)]
        self.assertEqual(self.sum_tree.autocomplete(['a'], 3), expected)

    def test_partial_common_prefix(self):
        tree = CompressedPrefixTree('average')
        tree.insert('car', 100.0, ['c', 'a', 'r'])
        tree.insert('door', 4.0, ['d', 'o', 'o', 'r'])
        tree.insert('danger', 6.0, ['d', 'a', 'n', 'g', 'e', 'r'])
        tree.insert('cat', 20.0, ['c', 'a', 't'])
        tree.insert('care', 30.0, ['c', 'a', 'r', 'e'])
        expected = [('danger', 6.0)]
        self.assertEqual(tree.autocomplete(['d', 'a'], 3), expected)

    def test_internal_full_match_prefix(self):
        tree = CompressedPrefixTree('average')
        tree.insert('car', 100.0, ['c', 'a', 'r'])
        tree.insert('door', 4.0, ['d', 'o', 'o', 'r'])
        tree.insert('danger', 6.0, ['d', 'a', 'n', 'g', 'e', 'r'])
        tree.insert('cat', 20.0, ['c', 'a', 't'])
        tree.insert('care', 30.0, ['c', 'a', 'r', 'e'])
        expected = [('car', 100.0), ('care', 30.0), ('cat', 20.0)]
        self.assertEqual(tree.autocomplete(['c'], 4), expected)


if __name__ == '__main__':
    unittest.main()
