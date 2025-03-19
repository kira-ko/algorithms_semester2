import unittest
from lab4.task5.src.main import compute_prefix_function

class TestPrefixFunction(unittest.TestCase):
    def test_case_1(self):
        s = "aaaAAA"
        expected_output = [0, 1, 2, 0, 0, 0]
        self.assertEqual(compute_prefix_function(s), expected_output)

    def test_case_2(self):
        s = "abacaba"
        expected_output = [0, 0, 1, 0, 1, 2, 3]
        self.assertEqual(compute_prefix_function(s), expected_output)

    def test_case_3(self):
        s = "a"
        expected_output = [0]
        self.assertEqual(compute_prefix_function(s), expected_output)


if __name__ == "__main__":
    unittest.main()