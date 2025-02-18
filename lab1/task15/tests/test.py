import unittest
from lab1.task15.src.main import remove_invalid_brackets

class TestRemoveInvalidBrackets(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(remove_invalid_brackets("()"), "()")

    def test_example2(self):
        self.assertEqual(remove_invalid_brackets("([)]"), "[]")

    def test_example3(self):
        self.assertEqual(remove_invalid_brackets("{[()]}"), "{[()]}")

    def test_example4(self):
        self.assertEqual(remove_invalid_brackets("{[("), "")

    def test_example5(self):
        self.assertEqual(remove_invalid_brackets("((()))"), "((()))")

if __name__ == '__main__':
    unittest.main()
