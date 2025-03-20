import unittest
from lab4.task7.src.main import longest_common_substring

class TestLongestCommonSubstring(unittest.TestCase):
    def test_exact_match(self):
        """Тест, где обе строки полностью совпадают"""
        s = "abcdef"
        t = "abcdef"
        self.assertEqual(longest_common_substring(s, t), (0, 0, 6))  # Однозначный ответ

    def test_no_common_substring(self):
        """Тест, где нет общей подстроки"""
        s = "abc"
        t = "xyz"
        self.assertEqual(longest_common_substring(s, t), (3, 0, 0))  # Однозначный ответ

    def test_unique_longest_substring(self):
        """Тест с единственной наибольшей общей подстрокой"""
        s = "abcdef"
        t = "zabcxy"
        self.assertEqual(longest_common_substring(s, t), (0, 1, 3))  # Единственная общая "abc"

    def test_single_character_match(self):
        """Тест, где общая подстрока – один символ"""
        s = "abcd"
        t = "xycz"
        self.assertEqual(longest_common_substring(s, t), (2, 2, 1))  # Единственное совпадение "c"

    def test_common_substring_at_end(self):
        """Тест, где наибольшая подстрока в конце"""
        s = "xyzabcd"
        t = "mnopabcd"
        self.assertEqual(longest_common_substring(s, t), (3, 4, 4))  # Единственная общая "abcd"

if __name__ == "__main__":
    unittest.main()

