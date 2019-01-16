"""CSC148 Assignment 2: Autocompleter classes

=== CSC148 Fall 2018 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This file contains the design of a public interface (Autocompleter) and two
implementation of this interface, SimplePrefixTree and CompressedPrefixTree.
You'll complete both of these subclasses over the course of this assignment.

As usual, be sure not to change any parts of the given *public interface* in the
starter code---and this includes the instance attributes, which we will be
testing directly! You may, however, add new private attributes, methods, and
top-level functions to this file.
"""
from __future__ import annotations
from typing import Any, List, Optional, Tuple


################################################################################
# The Autocompleter ADT
################################################################################
class Autocompleter:
    """An abstract class representing the Autocompleter Abstract Data Type.
    """
    def __len__(self) -> int:
        """Return the number of values stored in this Autocompleter."""
        raise NotImplementedError

    def insert(self, value: Any, weight: float, prefix: List) -> None:
        """Insert the given value into this Autocompleter.

        The value is inserted with the given weight, and is associated with
        the prefix sequence <prefix>.

        If the value has already been inserted into this prefix tree
        (compare values using ==), then the given weight should be *added* to
        the existing weight of this value.

        Preconditions:
            weight > 0
            The given value is either:
                1) not in this Autocompleter
                2) was previously inserted with the SAME prefix sequence
        """
        raise NotImplementedError

    def autocomplete(self, prefix: List,
                     limit: Optional[int] = None) -> List[Tuple[Any, float]]:
        """Return up to <limit> matches for the given prefix.

        The return value is a list of tuples (value, weight), and must be
        ordered in non-increasing weight. (You can decide how to break ties.)

        If limit is None, return *every* match for the given prefix.

        Precondition: limit is None or limit > 0.
        """
        raise NotImplementedError

    def remove(self, prefix: List) -> None:
        """Remove all values that match the given prefix.
        """
        raise NotImplementedError


################################################################################
# SimplePrefixTree (Tasks 1-3)
################################################################################
class SimplePrefixTree(Autocompleter):
    """A simple prefix tree.

    This class follows the implementation described on the assignment handout.
    Note that we've made the attributes public because we will be accessing them
    directly for testing purposes.

    === Attributes ===
    value:
        The value stored at the root of this prefix tree, or [] if this
        prefix tree is empty.
    weight:
        The weight of this prefix tree. If this tree is a leaf, this attribute
        stores the weight of the value stored in the leaf. If this tree is
        not a leaf and non-empty, this attribute stores the *aggregate weight*
        of the leaf weights in this tree.
    subtrees:
        A list of subtrees of this prefix tree.
    _length:
        the length of the SimplePrefixTree

    === Representation invariants ===
    - self.weight >= 0

    - (EMPTY TREE):
        If self.weight == 0, then self.value == [] and self.subtrees == [].
        This represents an empty simple prefix tree.
    - (LEAF):
        If self.subtrees == [] and self.weight > 0, this tree is a leaf.
        (self.value is a value that was inserted into this tree.)
    - (NON-EMPTY, NON-LEAF):
        If len(self.subtrees) > 0, then self.value is a list (*common prefix*),
        and self.weight > 0 (*aggregate weight*).

    - ("prefixes grow by 1")
      If len(self.subtrees) > 0, and subtree in self.subtrees, and subtree
      is non-empty and not a leaf, then

          subtree.value == self.value + [x], for some element x

    - self.subtrees does not contain any empty prefix trees.
    - self.subtrees is *sorted* in non-increasing order of their weights.
      (You can break ties any way you like.)
      Note that this applies to both leaves and non-leaf subtrees:
      both can appear in the same self.subtrees list, and both have a `weight`
      attribute.
    """
    value: Any
    weight: float
    subtrees: List[SimplePrefixTree]
    weight_type: str
    _length: int

    def __init__(self, weight_types: str) -> None:
        """Initialize an empty simple prefix tree.
        Precondition: weight_type == 'sum' or weight_type == 'average'.
        The given <weight_type> value specifies how the aggregate weight
        of non-leaf trees should be calculated (see the assignment handout
        for details).
        """
        self.value = []
        self.weight = 0.0
        self.subtrees = []
        self.weight_type = weight_types
        self._length = 0

    def __gt__(self, other: Any) -> Any:
        """
        compare weight
        """
        return self.weight > other.weight

    def get_subtree_node(self, prefix: List) -> Any:
        """
        return the node of subtree
        or -1 if it is leaf with no subtree

        """
        for subtree in self.subtrees:
            if not subtree.is_leaf():
                if subtree.value == self.value + [prefix[0]]:
                    return subtree
        return -1

    def update_leaf(self, weight: float, value: Any) -> int:
        """
        update the leaf and the weight of leaf
        """
        for tree in self.subtrees:
            if tree.value == value:
                tree.weight += weight
                return 0
        tree = self.create_tree(value, weight)
        tree._length = 1
        self.subtrees.append(tree)
        self.subtrees = sorted(self.subtrees)[::-1]
        return 1

    def __len__(self) -> int:
        """
        count number of leaves
        """
        return self._length

    def create_tree(self, value: Any, weight: float) -> SimplePrefixTree:
        """
        create a simpleprefix tree

        """
        tree = SimplePrefixTree(self.weight_type)
        tree.weight, tree.value = weight, value
        return tree

    def insert(self, value: Any, weight: float, prefix: List) -> None:
        """Insert the given value into this Autocompleter.

        The value is inserted with the given weight, and is associated with
        the prefix sequence <prefix>.

        If the value has already been inserted into this prefix tree
        (compare values using ==), then the given weight should be *added* to
        the existing weight of this value.

        Preconditions:
            weight > 0
            The given value is either:
                1) not in this Autocompleter
                2) was previously inserted with the SAME prefix sequence
        """
        self.insert_helper(value, weight, prefix)

    def insert_helper(self, value: Any, weight: float, prefix: List) -> int:
        """
        insert the value in to the tree
        """
        upgrade = lambda x: sum([subtree._length for subtree in x.subtrees])
        leaf_num = 0
        if len(prefix) == 0:
            leaf_num = self.update_leaf(weight, value)
            self.weight += weight
            self._length = upgrade(self)
        else:
            if self.get_subtree_node(prefix) == -1:
                tree = self.create_tree(self.value + [prefix[0]], 0)
                self.subtrees.append(tree)
                self.weight += weight
                tree.insert_helper(value, weight, prefix[1:])
                self._length = upgrade(self)
                self.subtrees = sorted(self.subtrees)[::-1]
                leaf_num = 1
            else:
                tree = self.get_subtree_node(prefix)
                tree.insert_helper(value, weight, prefix[1:])
                self.subtrees = sorted(self.subtrees)[::-1]
                self.weight += weight
                self._length = upgrade(self)
        if self.weight_type == 'average':
            self.weight = \
                sum([subtree._length * subtree.weight for subtree
                     in self.subtrees])\
                / self._length
        return leaf_num

    def find_node(self, prefix: List) -> Any:
        """
        find the node of given prefix
        """
        if len(prefix) == 0:
            return self
        for subtree in self.subtrees:
            if subtree.value == prefix:
                return subtree
        for subtree in self.subtrees:
            if prefix in subtree:
                return subtree.find_node(prefix)
        return -1

    def __contains__(self, item: Any) -> bool:
        """
        return true if the item in subtree
        """
        if len(self.subtrees) == 0:
            return self.value == item
        else:
            for subtree in self.subtrees:
                if item in subtree:
                    return True
            return self.value == item

    def get_leaf(self) -> List:
        """
        return a list of leaf

        """
        if self.is_leaf():
            return [self]
        else:
            temp = []
            for tree in self.subtrees:
                temp += tree.get_leaf()
            return temp

    def autocomplete(self, prefix: List,
                     limit: Optional[int] = None) -> List[Tuple[Any, float]]:
        """Return up to <limit> matches for the given prefix.

        The return value is a list of tuples (value, weight), and must be
        ordered in non-increasing weight. (You can decide how to break ties.)

        If limit is None, return *every* match for the given prefix.

        Precondition: limit is None or limit > 0.
        """
        auto_helper = lambda temp: [(i.value, i.weight) for i in temp]

        node = self.find_node(prefix)
        if node == -1:
            return []
        else:
            temp = node.get_leaf()
            if limit is not None:
                if limit < len(temp):
                    temp = sorted(temp[:limit])[::-1]
                    result = auto_helper(temp)
                    return result
                else:
                    temp = sorted(temp)[::-1]
                    return auto_helper(temp)
            else:
                temp = sorted(temp)[::-1]
                return auto_helper(temp)

    def remove(self, prefix: List) -> None:
        """Remove all values that match the given prefix.
        """
        if len(prefix) == 0:
            self.subtrees = []
            self.weight = 0
            self._length = 0
        self.helper1(prefix)

    def helper1(self, prefix: List) -> Optional[SimplePrefixTree, None]:
        """
        method remove
        """
        upgrade = lambda x: sum([subtree._length for subtree in x.subtrees])
        upgrade_weight = lambda x: \
            sum([subtree.weight for subtree in x.subtrees])
        if prefix == self.value:
            return self
        for subtree in self.subtrees:
            if not subtree.is_leaf() and self.value + \
                    [subtree.value[len(self.value)]] == \
                    prefix[:len(self.value) + 1]:
                stuff = subtree.helper1(prefix)
                if stuff is not None:
                    self._length = upgrade(self)
                    self.weight = upgrade_weight(self)
                    if self.weight_type == 'average':
                        self.weight = self.weight / self._length
                    self.subtrees.remove(subtree)
                if len(self.subtrees) == 0:
                    return self
                else:
                    self._length = upgrade(self)
                    self.weight = upgrade_weight(self)
                    if self.weight_type == 'average':
                        self.weight = self.weight / self._length
                    return None
        return None

    def is_empty(self) -> bool:
        """Return whether this simple prefix tree is empty."""
        return self.weight == 0.0

    def is_leaf(self) -> bool:
        """Return whether this simple prefix tree is a leaf."""
        return self.weight > 0 and self.subtrees == []

    def __str__(self) -> str:
        """Return a string representation of this tree.

        You may find this method helpful for debugging.
        """
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + \
                f'{self.value} ({self.weight}) ({self._length})\n'
            for subtree in self.subtrees:
                s += subtree._str_indented(depth + 1)
            return s

    def get_all_node(self) -> list:
        """
        get all the node in the tree
        """
        if self.is_empty():
            return [self]
        elif self.is_leaf():
            return [self]
        else:
            temp = [self]
            for subtree in self.subtrees:
                temp += subtree.get_all_node()
            return temp

    def get_parent(self, node: SimplePrefixTree) -> SimplePrefixTree:
        """
        precondition: node is in the tree
        return the parent of the node from the tree
        """
        for subtree in self.subtrees:
            if node.value == subtree.value:
                return self
        for subtree in self.subtrees:
            if node.value in subtree:
                return subtree.get_parent(node)
        return self

    def compress(self) -> SimplePrefixTree:
        """
        compress the SimplePrefixTree
        """
        temp = self.get_all_node()[1:]
        for tree in temp:
            if len(tree.subtrees) == 1 and not tree.subtrees[0].is_leaf():
                added_tree = tree.subtrees[0]
                parent_tree = self.get_parent(tree)
                parent_tree.subtrees.remove(tree)
                parent_tree.subtrees.append(added_tree)
                parent_tree.subtrees.sort(reverse=True)
        if len(self.subtrees) == 1:
            temp = self.subtrees[0]
            return temp
        return self

    def copy(self) -> SimplePrefixTree:
        """
        copy a SimplePrefixTree, make it have different id
        """
        tree = SimplePrefixTree(self.weight_type)
        tree.subtrees = [t.copy() for t in self.subtrees]
        tree.weight, tree.value, tree._length = \
            self.weight, self.value, self._length
        return tree

################################################################################
# CompressedPrefixTree (Task 6)
################################################################################
class CompressedPrefixTree(Autocompleter):
    """A compressed prefix tree implementation.

    While this class has the same public interface as SimplePrefixTree,
    (including the initializer!) this version follows the implementation
    described on Task 6 of the assignment handout, which reduces the number of
    tree objects used to store values in the tree.

    === Attributes ===
    value:
        The value stored at the root of this prefix tree, or [] if this
        prefix tree is empty.
    weight:
        The weight of this prefix tree. If this tree is a leaf, this attribute
        stores the weight of the value stored in the leaf. If this tree is
        not a leaf and non-empty, this attribute stores the *aggregate weight*
        of the leaf weights in this tree.
    subtrees:
        A list of subtrees of this prefix tree.
    simple_tree:
        a simpleprefixtree to help implement of this class

    === Representation invariants ===
    - self.weight >= 0

    - (EMPTY TREE):
        If self.weight == 0, then self.value == [] and self.subtrees == [].
        This represents an empty simple prefix tree.
    - (LEAF):
        If self.subtrees == [] and self.weight > 0, this tree is a leaf.
        (self.value is a value that was inserted into this tree.)
    - (NON-EMPTY, NON-LEAF):
        If len(self.subtrees) > 0, then self.value is a list (*common prefix*),
        and self.weight > 0 (*aggregate weight*).

    - **NEW**
      This tree does not contain any compressible internal values.
      (See the assignment handout for a definition of "compressible".)

    - self.subtrees does not contain any empty prefix trees.
    - self.subtrees is *sorted* in non-increasing order of their weights.
      (You can break ties any way you like.)
      Note that this applies to both leaves and non-leaf subtrees:
      both can appear in the same self.subtrees list, and both have a `weight`
      attribute.
    """
    value: Optional[Any]
    weight: float
    subtrees: List[CompressedPrefixTree]
    weight_type: str
    simple_tree: SimplePrefixTree

    def __init__(self, weight_types: str) -> None:
        """Initialize an empty simple prefix tree.

        Precondition: weight_type == 'sum' or weight_type == 'average'.

        The given <weight_type> value specifies how the aggregate weight
        of non-leaf trees should be calculated (see the assignment handout
        for details).
        """
        self.value = []
        self.weight = 0.0
        self.subtrees = []
        self.weight_type = weight_types
        self.simple_tree = SimplePrefixTree(weight_types)

    def __len__(self) -> int:
        """Return the number of values stored in this Autocompleter."""
        return len(self.simple_tree)

    def insert(self, value: Any, weight: float, prefix: List) -> None:
        """Insert the given value into this Autocompleter.

        The value is inserted with the given weight, and is associated with
        the prefix sequence <prefix>.

        If the value has already been inserted into this prefix tree
        (compare values using ==), then the given weight should be *added* to
        the existing weight of this value.

        Preconditions:
            weight > 0
            The given value is either:
                1) not in this Autocompleter
                2) was previously inserted with the SAME prefix sequence
        """
        self.simple_tree.insert(value, weight, prefix)
        temp = self.simple_tree.copy()
        temp = temp.compress()
        self.subtrees = temp.subtrees
        self.value = temp.value
        self.weight = temp.weight

    def __contains__(self, item: Any) -> bool:
        """
        return true if the item in subtree

        """
        if len(self.subtrees) == 0:
            return self.value == item
        else:
            for subtree in self.subtrees:
                if item in subtree:
                    return True
            return self.value == item

    def autocomplete(self, prefix: List,
                     limit: Optional[int] = None) -> List[Tuple[Any, float]]:
        """Return up to <limit> matches for the given prefix.

        The return value is a list of tuples (value, weight), and must be
        ordered in non-increasing weight. (You can decide how to break ties.)

        If limit is None, return *every* match for the given prefix.

        Precondition: limit is None or limit > 0.
        """
        return self.simple_tree.autocomplete(prefix, limit)

    def remove(self, prefix: List) -> None:
        """Remove all values that match the given prefix.
        """
        self.simple_tree.remove(prefix)
        temp = self.simple_tree.copy()
        temp = temp.compress()
        self.subtrees = temp.subtrees
        self.value = temp.value
        self.weight = temp.weight

    def is_empty(self) -> bool:
        """Return whether this simple prefix tree is empty."""
        return self.weight == 0.0

    def is_leaf(self) -> bool:
        """Return whether this simple prefix tree is a leaf."""
        return self.weight > 0 and self.subtrees == []

    def __str__(self) -> str:
        """Return a string representation of this tree.

        You may find this method helpful for debugging.
        """
        return self._str_indented()

    def _str_indented(self, depth: int = 0) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            s = '  ' * depth + \
                f'{self.value} ({self.weight})\n'
            for subtree in self.subtrees:
                s += subtree._str_indented(depth + 1)
            return s


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-nested-blocks': 4
    })
