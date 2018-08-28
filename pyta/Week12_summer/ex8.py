"""
Implement the get_sorted_order function.
"""
from typing import Union, List


class BinarySearchTree:
    """
    A class representing a BinarySearchTree.

    value - The value of the BinarySearchTree's root
    left - The root node of this BinarySearchTree's left subtree.
    right - The root node of this BinarySearchTree's right subtree.
    """
    value: int
    left: Union['BinarySearchTree', None]
    right: Union['BinarySearchTree', None]

    def __init__(self, value: int, left: 'BinarySearchTree' = None,
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


def get_sorted_order(tree: BinarySearchTree) -> List[int]:
    """
    Return the items in tree in sorted order.

    You may not use sorted() or sort() for this. You may only use properties
    of the BST itself.

    Assume all values in tree are ints.

    >>> get_sorted_order(None)
    []
    >>> get_sorted_order(BinarySearchTree(4, BinarySearchTree(2),
    ...                                      BinarySearchTree(6,
    ...                                                   BinarySearchTree(5))))
    [2, 4, 5, 6]
    """
    if tree is None:
        return []
    return get_sorted_order(tree.left) + \
           [tree.value] + \
           get_sorted_order(tree.right)





if __name__ == '__main__':
    t1 = BinarySearchTree(5, BinarySearchTree(2, right=BinarySearchTree(3)))
    t2 = BinarySearchTree(8, BinarySearchTree(7), BinarySearchTree(9))
    t = BinarySearchTree(6, t1, t2)

    # t is the BST:
    #           6
    #        5        8
    #  2           7     9
    #     3

    assert get_sorted_order(None) == []
    assert get_sorted_order(t1) == [2, 3, 5]
    assert get_sorted_order(t2) == [7, 8, 9]
    assert get_sorted_order(t) == [2, 3, 5, 6, 7, 8, 9]

    import python_ta

    python_ta.check_all(config='ex8_pyta.txt')
