import unittest
from lab1.task17.src.main import horse

class TestHorse(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(horse(1), 8)

    def test_case_2(self):
        self.assertEqual(horse(2), 16)

    def test_case_3(self):
        self.assertEqual(horse(3), 36)

    def test_case_4(self):
        self.assertEqual(horse(4), 82)

if __name__ == "__main__":
    unittest.main()