import unittest
from lab4.task2.src.main import count_palindromic_triplets


class TestTreasureMap(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(count_palindromic_triplets("treasure"), 8)
        self.assertEqual(count_palindromic_triplets("you will never find the treasure"), 146)

    def test_minimum_length(self):
        self.assertEqual(count_palindromic_triplets("abc"), 0)  # Только одна возможная тройка

    def test_mixed_characters(self):
        self.assertEqual(count_palindromic_triplets("racecar"), 9)  # Разные палиндромные комбинации
        self.assertEqual(count_palindromic_triplets("abba"), 2)  # Палиндромные сочетания

if __name__ == "__main__":
    unittest.main()