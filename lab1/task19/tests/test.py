import unittest
from lab1.task19.src.main import matrix_chain_order


class TestMatrixChainOrder(unittest.TestCase):
    """пример из условия задачи"""
    def test_case_1(self):
        dimensions = [10, 50, 90, 20]
        expected = "((AA)A)"
        result = matrix_chain_order(dimensions)
        self.assertEqual(result, expected)

    def test_case_2(self):
        dimensions = [10, 20, 30] #(10, 20, 20, 30)
        expected = "(AA)"
        result = matrix_chain_order(dimensions)
        self.assertEqual(result, expected)

    '''одна матрица'''
    def test_case_3(self):
        dimensions = [10, 20]
        expected = "A"
        result = matrix_chain_order(dimensions)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()