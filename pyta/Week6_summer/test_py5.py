# Import the student solution
from ex5 import *
import unittest


class ExerciseTests(unittest.TestCase):
    def test_client_code(self):
        """
        Tests the client code to make sure the exercise passes it.
        """
        single_int = 1
        self.assertEqual(get_all_evens(single_int), [])

        lst = [1, 2, 3, 4]
        self.assertEqual(sorted(get_all_evens(lst)), [2, 4])

        nested_lst = [1, [2, 3, [4]], [[4], 6]]
        self.assertEqual(sorted(get_all_evens(nested_lst)), [2, 4, 4, 6])

    def test_hidden(self):
        """
        The hidden test for students.
        """
        # Test a single odd int
        to_test = 9
        expected_result = []
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a single even int
        to_test = 4
        expected_result = [4]
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a singly-nested list with no evens
        to_test = [1, 3, 5, 7, 9]
        expected_result = []
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a singly-nested list with only evens
        to_test = [2, 4, 6, 8, 10]
        expected_result = [2, 4, 6, 8, 10]
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a heavily-nested list with only odds
        to_test = [[[[1]], [3, [[[5]]]]], [[7], [9, [[[11]], [13]]]]]
        expected_result = []
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a heavily-nested list with only evens
        to_test = [[[[2]], [4, [[[6]]]]], [[8], [10, [[[12]], [14]]]]]
        expected_result = [2, 4, 6, 8, 10, 12, 14]
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)

        # Test a heavily-nested list with both odds and evens
        to_test = [[[[5]], [2, [[[7]]]]], [[8], [9, [[[4]], [6]]]]]
        expected_result = [2, 4, 6, 8]
        actual_result = sorted(get_all_evens(to_test))

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main(exit=False)