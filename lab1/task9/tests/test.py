import unittest
from lab1.task9.src.main import min_print

class TestMinPrintCost(unittest.TestCase):

    def test_case_1(self):
        N = 980
        A = [1, 9, 90, 900, 1000, 10000, 10000]
        result = min_print(N, A)
        self.assertEqual(result, 882)

    def test_case_2(self):
        N = 980
        A = [1, 10, 100, 1000, 900, 10000, 10000]
        result = min_print(N, A)
        self.assertEqual(result, 900)

    '''минимальный случай'''
    def test_case_3(self):
        N = 1
        A = [5, 40, 300, 2500, 10000, 15000, 20000]
        result = min_print(N, A)
        self.assertEqual(result, 5)

    '''граничный случай между тарифами (n=10)'''
    def test_case_4(self):
        N = 10
        A = [2, 15, 120, 1100, 10500, 90000, 800000]
        result = min_print(N, A)
        self.assertEqual(result, 15)

    '''комбинация выгоднее'''
    def test_case_5(self):
        N = 15
        A = [2, 18, 100, 1000, 9000, 80000, 700000]
        result = min_print(N, A)
        self.assertEqual(result, 30)

    '''более крупная партия'''
    def test_case_6(self):
        N = 9999
        A = [1, 9, 80, 700, 6500, 50000, 400000]
        result = min_print(N, A)
        self.assertEqual(result, 6500)

    '''А1 всегда выгоднее'''
    def test_case_7(self):
        N = 500
        A = [1, 20, 250, 3000, 35000, 50000, 400000]
        result = min_print(N, A)
        self.assertEqual(result, 500)

    '''граничный случай n=1000000'''
    def test_case_8(self):
        N = 1000000
        A = [5, 40, 350, 2500, 20000, 150000, 900000]
        result = min_print(N, A)
        self.assertEqual(result, 900000)

    '''дешевле брать больше листов'''
    def test_case_9(self):
        N = 9500
        A = [2, 15, 140, 1200, 11000, 100000, 900000]
        result = min_print(N, A)
        self.assertEqual(result, 11000)

    def test_case_10(self):
        N = 5
        A = [1, 10, 100, 1000, 900, 10000, 10000]
        result = min_print(N, A)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()

