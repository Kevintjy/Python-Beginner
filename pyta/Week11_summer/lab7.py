"""
The BinaryTree class for Lab 7.
"""
from typing import Any


class BinaryTree:
    """
    A class representing a BinaryTree.

    value - The value of the BinaryTree's root
    left - The root node of this BinaryTree's left subtree.
    right - The root node of this BinaryTree's right subtree.
    """
    value: Any
    left: 'BinaryTree'
    right: 'BinaryTree'

    def __init__(self, value: Any, left: 'BinaryTree' = None,
                 right: 'BinaryTree' = None) -> None:
        """
        Initialize this BinaryTree with the root value value, left subtree left,
        and right subtree right.
        """
        self.value = value
        self.left = left
        self.right = right

    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this BinaryTree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).

        >>> t1 = BinaryTree(1, BinaryTree(3, BinaryTree(4), BinaryTree(6)))
        >>> print(t1)
          1
          3
        4   6
        >>> t2 = BinaryTree(9, BinaryTree(7), BinaryTree(5))
        >>> print(t2)
          9
        7   5
        >>> t = BinaryTree(0, t1, t2)
        >>> print(t)
              0
          1       9
          3     7   5
        4   6
        """
        children = []
        if self.left:
            children.append(self.left)

        if self.right:
            children.append(self.right)

        child_strings = [str(child).split('\n') for child in children]

        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])

        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]

        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                child_length = max([len(line) for line in child])

                if i < len(child):
                    padding_needed = child_length - len(child[i])
                    new_string[i].append(child[i] + " " * padding_needed)
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * child_length)

        # Put 3 spaces between each subtree
        new_string_joined = [(' ' * 3).join(child) for child in new_string]

        # Add in the value of the current Tree
        str_width = 0
        if new_string_joined:
            str_width = len(new_string_joined[0])

        left_padding = str_width // 2
        right_padding = (str_width - str_width // 2) - 1

        new_string_joined.insert(0, "{}{}{}".format(" " * left_padding,
                                                    self.value,
                                                    " " * right_padding))

        new_string_joined = [line.rstrip() for line in new_string_joined]

        # Return the new string
        return "\n".join(new_string_joined)

    def get_internal_values(self):
        """
        return a list containing all values in a tree
        """
        if self.left is None and self.right is None:
            return [self.value]
        if self.left is not None and self.right is not None:
            return [self.value] + self.left.get_internal_values() + self.right.get_internal_values()
        if self.left is not None:
            return [self.value] + self.left.get_internal_values()
        if self.right is not None:
            return [self.value] + self.right.get_internal_values()


    def get_max_depth(self):
        """
        get the max depth
        """
        if self.left is None and self.right is None:
            return 0
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.get_max_depth(), self.right.get_max_depth())
        if self.left is not None:
            return 1 + self.left.get_max_depth()
        if self.right is not None:
            return 1 + self.right.get_max_depth()


def get_depth_of(t, value):
    """
    return the depth of the value in the tree
    """
    if t is None:
        return -1
    if t.value == value:
        return 0
    if get_depth_of(t.left, value) > -1:
        return get_depth_of(t.left, value) + 1
    if get_depth_of(t.right, value) > -1:
        return get_depth_of(t.right, value) + 1
    return -1


def get_values_at_depth(t, level):
    """
    return the all the nodes in the tree's level
    """
    if t is None:
        return []
    if level == 0:
        return [t.value]
    else:
        return get_values_at_depth(t.left, level - 1) +\
               get_values_at_depth(t.right, level - 1)


def copy(t):
    if t is None:
        return None
    return BinaryTree(t.value, left=copy(t.left), right=copy(t.right))

def print_level_order(t):
    """
    print all the values in level order
    """
    result = []
    level = 0
    depth = t.get_max_depth()
    while level <= depth:
        result.append(get_values_at_depth(t, level))
        level += 1
    for i in sum(result, []):
        print(i)


def insert_before(t, to_insert, to_find):
    """
    add the in_insert before the to find in the tree
    and then to_find is the to_insert.left
    """
    if t.left is None and t.right is None:
        return -1
    if t.left and t.left.value == to_find:
        temp = t.left
        t.left = BinaryTree(to_insert, temp)
        return
    if t.right and t.right.value == to_find:
        temp = t.right
        t.right = BinaryTree(to_insert, temp)
        return
    if t.left:
        insert_before(t.left, to_insert, to_find)
    if t.right:
        insert_before(t.right,to_insert, to_find)


def create_tree():
    global large_tree
    t1 = BinaryTree(2,left=BinaryTree(5, right=BinaryTree(2, left=BinaryTree(3))))
    t2 = BinaryTree(4, left=BinaryTree(6, left=BinaryTree(3), right=BinaryTree(4)), right=BinaryTree(7))
    large_tree = BinaryTree(1, left=t1, right=t2)


if __name__ == '__main__':
    t1 = BinaryTree(1, left=BinaryTree(3))
    t2 = BinaryTree(2)
    t = BinaryTree(0, left=t1, right=t2)
    create_tree()
    insert_before(large_tree, 9, 7),
    print(large_tree)
    print('============')


