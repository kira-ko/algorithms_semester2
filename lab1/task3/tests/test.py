import unittest
from lab1.task3.src.main import max_revenue_calculate

class TestMaxAdRevenue(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_revenue_calculate([23], [39]), 897)

    def test_case_2(self):
        self.assertEqual(max_revenue_calculate([1, 3, -5], [-2, 4, 1]), 23)

    def test_case_3(self):
        self.assertEqual(max_revenue_calculate([-1, -2, -3], [-3, -2, -1]), 14)

    def test_case_4(self):
        self.assertEqual(max_revenue_calculate([0, 0, 0], [0, 0, 0]), 0)

if __name__ == "__main__":
    unittest.main()