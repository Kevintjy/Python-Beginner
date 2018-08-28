# Import the student solution
from ex7 import *
import unittest


class ExerciseTests(unittest.TestCase):
    def test_client_code(self):
        """
        Tests the client code to make sure the exercise passes it.
        """
        t1 = BinaryTree(3, BinaryTree(5, right=BinaryTree(2)))
        t2 = BinaryTree(4, BinaryTree(6), BinaryTree(7))
        t = BinaryTree(1, t1, t2)

        # t is the Tree from the handout:
        #       1
        #     3     4
        # 5       6   7
        #   2

        self.assertEqual(get_largest_height_difference(None), 0)
        self.assertEqual(get_largest_height_difference(t1), 2)
        self.assertEqual(get_largest_height_difference(t2), 0)
        self.assertEqual(get_largest_height_difference(t), 2)

    def test_hidden(self):
        """
        The hidden test for students.
        """
        # A leaf
        leaf = BinaryTree(3)
        self.assertEqual(get_largest_height_difference(leaf), 0)

        # One sided Binary Tree
        one_sided = BinaryTree(1, BinaryTree(2, BinaryTree(3, BinaryTree(4, BinaryTree(5)))))
        self.assertEqual(get_largest_height_difference(one_sided), 4)

        # One sided Binary Tree with a mixed child
        one_sided_mixed = BinaryTree(1, right=BinaryTree(2, BinaryTree(3, right=BinaryTree(4, BinaryTree(5)))))
        self.assertEqual(get_largest_height_difference(one_sided_mixed), 4)

        # Multiple levels
        #               1
        #         2           3
        #      8     1     2    4
        #   9    8     7    6     5
        # 11         3              6
        #                             7

        left = BinaryTree(2, BinaryTree(8, BinaryTree(9, BinaryTree(11)),
                                        BinaryTree(8)),
                          BinaryTree(1, right=BinaryTree(7, BinaryTree(3))))

        right = BinaryTree(3, BinaryTree(2, right=BinaryTree(6)),
                           BinaryTree(4, right=BinaryTree(5, right=BinaryTree(6, right=BinaryTree(7)))))

        t = BinaryTree(1, left, right)

        self.assertEqual(get_largest_height_difference(left), 2)
        self.assertEqual(get_largest_height_difference(right), 3)
        self.assertEqual(get_largest_height_difference(t), 3)


if __name__ == "__main__":
    unittest.main(exit=False)