import unittest
from lab1.task14.src.main import max_expression_value

class MaxExpressionValueTest(unittest.TestCase):

    '''Тест из примера 1'''
    def test_case_1(self):
        expression = '1+5'
        result = max_expression_value(expression)
        self.assertEqual(result, 6)

    '''Тест из примера 2'''
    def test_case_2(self):
        expression = '5-8+7*4-8+9'
        result = max_expression_value(expression)
        self.assertEqual(result, 200)

    '''Одни скобки'''
    def test_case_3(self):
        expression = '3+2*5'
        result = max_expression_value(expression)
        self.assertEqual(result, 25)

    '''Две скобки'''
    def test_case_4(self):
        expression = '1+2*3+4'
        result = max_expression_value(expression)
        self.assertEqual(result, 21)

    def test_case_5(self):
        expression = '2+3*4-6+2*5'
        result = max_expression_value(expression)
        self.assertEqual(result, 80)


if __name__ == "__main__":
    unittest.main()