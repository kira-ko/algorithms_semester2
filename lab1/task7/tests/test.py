import unittest
from lab1.task7.src.main import max_boots

class TestMaxBoots(unittest.TestCase):

    def test_case_1(self):
        k, n = 10, 3
        times = [2, 6, 8]
        self.assertEqual(max_boots(k, n, times), 2)

    def test_case_2(self):
        k, n = 3, 2
        times = [5, 7]
        self.assertEqual(max_boots(k, n, times), 0)

    def test_case_3(self):
        k, n = 5, 1
        times = [3]
        self.assertEqual(max_boots(k, n, times), 1)

    def test_case_4(self):
        k, n = 10, 4
        times = [3, 3, 3, 3]
        self.assertEqual(max_boots(k, n, times), 3)

    def test_case_5(self):
        k, n = 1000, 500
        times = [1] * 500
        self.assertEqual(max_boots(k, n, times), 500)

    def test_case_6(self):
        k, n = 1, 3
        times = [1, 2, 3]
        self.assertEqual(max_boots(k, n, times), 1)

if __name__ == '__main__':
    unittest.main()