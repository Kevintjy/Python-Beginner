"""
The BinarySearchTree class for Lab 8
"""
from typing import Any, List, Union


class BinarySearchTree:
    """
    A class representing a BinarySearchTree.

    value - The value of the BinarySearchTree's root
    left - The root node of this BinarySearchTree's left subtree.
    right - The root node of this BinarySearchTree's right subtree.
    """
    value: Any
    left: Union['BinarySearchTree', None]
    right: Union['BinarySearchTree', None]

    def __init__(self, value: Any, left: 'BinarySearchTree' = None,
                 right: 'BinarySearchTree' = None) -> None:
        """
        Initialize this BinarySearchTree with the root value value, left subtree
        left, and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        Return the string representation of this BinarySearchTree, such that the
        root node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).

        >>> t1 = BinarySearchTree(4, BinarySearchTree(2, BinarySearchTree(1),
        ...                                              BinarySearchTree(3)))
        >>> print(t1)
                   4
             2
          1     3
        """
        children = []
        if self.left:
            children.append(str(self.left))
        else:
            children.append("")

        if self.right:
            children.append(str(self.right))
        else:
            children.append("")

        child_strings = [child.split('\n') for child in children]

        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])

        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]
        child_lengths = []

        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                child_length = max([len(line) for line in child])
                child_lengths.append(child_length)

                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed)
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)

        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]

        # Add in the value of the current Tree
        left_padding = child_lengths[0] + 2

        new_string_joined.insert(0, "{}{}".format(" " * left_padding,
                                                  self.value))

        new_string_joined = [line.rstrip() for line in new_string_joined]

        # Return the new string
        return "\n".join(new_string_joined).rstrip()


def insert(t: Union['BinarySearchTree', None], value: Any) -> bool:
    """
    Insert value into t, maintaining the BinarySearchTree properties. Return
    the root node of t.

    Pre-condition: value is not in t.

    >>> print(insert(None, 2))
      2
    >>> print(insert(BinarySearchTree(4, BinarySearchTree(2),
    ...                                  BinarySearchTree(6,
    ...                                      BinarySearchTree(5))), 3))
            4
      2           6
         3     5
    """
    if t is None:
        return BinarySearchTree(value)

    if value < t.value:
        t.left = insert(t.left, value)
    else:
        t.right = insert(t.right, value)

    return t

def create_bst():
    global bst
    bst = BinarySearchTree(7)
    insert(bst, 4)
    insert(bst, 15)
    insert(bst, 1)
    insert(bst, 10)
    insert(bst, 18)
    insert(bst, 3)
    insert(bst, 8)
    insert(bst, 12)
    insert(bst, 2)

def find_min(bst):
    if bst.left:
        return find_min(bst.left)
    return bst.value

def find_max(bst):
    if bst.right:
        return find_max(bst.right)
    return bst.value

def delete(t, value):

    if t is None:
        return None
    if t.value > value:
        t.right = delete(t.right, value)
    if t.value < value:
        t.left = delete(t.left, value)
    else:
        if not t.left and not t.right:
            return None
        if not t.left and t.right:
            return t.right
        if not t.right and t.left:
            return t.left

        min_value = find_min(t)
        t.value = min_value
        t.right = delete(t.right, min_value)
    return t

def is_valid_bst(t):
    if t is None:
        return True
    if t.value < find_min(t) or t.value > find_max(t):
        return False
    return is_valid_bst(t.left) and is_valid_bst(t.right)

def count_nodes(t):
    if t is None:
        return 0
    return 1 + count_nodes(t.left) + count_nodes(t.right)

def find_nth_smallest(t, n):
    if count_nodes(t.left) + 1 > n:
        return find_nth_smallest(t.left, n)
    if count_nodes(t.left) + 1 == n:
        return t.value
    else:
        return find_nth_smallest(t.right,n - count_nodes(t.left) - 1)


def rotate_right(t):
    if not t.left:
        return t
    else:
        new_root = t.left
        temp1 = new_root.right
        new_root.right = BinarySearchTree(t.value, right=t.right, left=temp1)
        return new_root





if __name__ == '__main__':
    t = BinarySearchTree(10)
    insert(t, 8)
    insert(t, 6)
    insert(t, 9)
    insert(t, 12)
    create_bst()
    print(bst)
    print('=================')
    print(rotate_right(bst))

    # import doctest
    #
    # doctest.testmod()

