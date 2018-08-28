"""
The Tree class for Lab 6.
"""
from typing import Any, List


class Tree:
    """
    A class representing a Tree.

    value - The value of the Tree's root
    children - The root nodes of the children of this Tree.
    """
    value: Any
    children: List['Tree']

    def __init__(self, value: Any, children: List['Tree'] = None) -> None:
        """
        Initialize this Tree with the root value value and children children.
        """
        self.value = value

        # We make this a copy of the list children, in case it gets modified
        # at some point elsewhere.
        self.children = children[:] if children else []

    # For convenience when trying to make a Tree.
    def __str__(self) -> str:
        """
        Return the string representation of this Tree, such that the root
        node is at the top, and all subtrees are below it. Every line of
        the string has the same length (being padded with spaces if needed).

        >>> t1 = Tree(1, [Tree(3, [Tree(4), Tree(6)])])
        >>> print(t1)
          1
          3
        4   6
        >>> t2 = Tree(2, [Tree(8)])
        >>> print(t2)
        2
        8
        >>> t3 = Tree(9, [Tree(7), Tree(5)])
        >>> print(t3)
          9
        7   5
        >>> children = [t1, t2, t3]
        >>> t = Tree(0, children)
        >>> print(t)
                0
          1     2     9
          3     8   7   5
        4   6
        """
        child_strings = [str(child).split('\n') for child in self.children]

        # Get the maximum number of lines from a child's string
        max_lines = 0
        if child_strings:
            max_lines = max([len(child) for child in child_strings])

        # Create a list with max_lines empty lists in it
        new_string = [[] for _ in range(max_lines)]

        # Join each line of each child's string
        for i in range(max_lines):
            for child in child_strings:
                if i < len(child):
                    new_string[i].append(child[i])
                else:
                    # If there is no such line, just pad it with spaces
                    new_string[i].append(" " * len(child[0]))

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

        # Return the new string
        return "\n".join(new_string_joined)

    def count_occurrences(self, value):
        """
        count the occurrences of the value appear in the tree
        """
        if self.value == value:
            return 1 + sum([child.count_occurrences(value) for child in self.children])
        return sum([child.count_occurrences(value) for child in self.children])


    def get_internal_values(self):
        """
        get the node which is not the leaf in pre_order
        """
        if self.children == []:
            return []
        return [self.value] + sum([child.get_internal_values() for child in self.children],[])

    def get_depth_of(self, value):
        """
        get the depth of the value in the tree
        """
        if self.value == value:
            return 0
        for child in self.children:
            if child.get_depth_of(value) != -1:
                return child.get_depth_of(value) + 1
        return -1


    def get_values_at_depth(self, depth):
        """
        get the value in a depth of a tree
        """
        if depth == 0:
            return [self.value]
        return sum([child.get_values_at_depth(depth-1) for child in self.children],[])

    def get_max_branching_factor(self):
        """
        get max branching factor of a tree
        """
        if self.children == []:
            return 1
        return 1 + max([child.get_max_branching_factor() for child in self.children])


    def copy(self):
        create_tree()
        s = Tree(self.value,self.children)
        return s



    def print_level_order(self):
        """
        print tree in level order
        """
        level = 0
        depth = self.get_max_branching_factor()
        result = []
        while level <= depth:
            result +=self.get_values_at_depth(level)
            level += 1
        return result



    def add_subtree_to(self,tree, value):
        """
        add the tree after the value
        """
        if self.value == value:
            self.children.append(tree)
            return True
        for node in self.children:
            flag = node.add_subtree_to(tree,value)
            if flag:
                return True
        return False

def create_tree():
    global t
    t1 = Tree(1,[Tree(4,[Tree(6)]),Tree(3), Tree(2)])
    t2 = Tree(7)
    t3 = Tree(3,[Tree(5),Tree(8,[Tree(9),Tree(1)])])
    t4 = Tree(8)
    t = Tree(5,[t1,t2,t3,t4])


if __name__ == '__main__':
    create_tree()
    print(t)
    print('==============')
    print(t.get_depth_of(1))
    assert t.count_occurrences(3) == 2
    assert t.count_occurrences(1) == 2
    assert t.count_occurrences(5) == 2
    assert t.count_occurrences(2) == 1

    assert t.get_internal_values() == [5, 1, 4, 3, 8]

    assert t.get_depth_of(1) == 1
    assert t.get_depth_of(8) == 2

    assert t.get_values_at_depth(0) == [5]
    assert t.get_values_at_depth(1) == [1,7,3,8]
    assert t.get_values_at_depth(3) == [6,9,1]

    assert t.get_max_branching_factor() == 4
    t.print_level_order()
    t.add_subtree_to(Tree(4,[Tree(999), Tree(888)]),3)
    print('===========')
    print(t)
    import python_ta
    # python_ta.check_all(config="lab_pyta.txt")
