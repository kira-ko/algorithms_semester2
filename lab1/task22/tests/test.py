import unittest
from lab1.task22.src.main import cute_patterns_main, cute_patterns

class TestNicePatterns(unittest.TestCase):
    def test_case_1(self):
        """Минимальный случай 1x1
        поле можно покрыть только двумя способами"""
        self.assertEqual(cute_patterns_main(1, 1), 2)

    def test_case_2(self):
        """Поле 2x2
        2^4=16 Минус два узора (все черные и все белые)"""
        self.assertEqual(cute_patterns_main(2, 2), 14)

    def test_case_3(self):
        """Длинный узкий двор 1x4
        каждая клетка может быть либо белой либо черной, запрещенных нет. 2^4=16"""
        self.assertEqual(cute_patterns_main(1, 4), 16)

    def test_case_4(self):
        """двор 4x1"""
        self.assertEqual(cute_patterns_main(4, 1), 16)

    def test_case_5(self):
        """Прямоугольное поле 3x3"""
        self.assertEqual(cute_patterns_main(3, 3), 322)


if __name__ == "__main__":
    unittest.main()