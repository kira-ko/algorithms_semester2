import unittest
from lab3.task11.src.main import alchemy_reactions
from collections import deque, defaultdict


class TestAlchemyReactions(unittest.TestCase):

    def setUp(self):
        # Устанавливаем общий тестовый набор реакций
        self.reactions = defaultdict(list)
        self.reactions["Aqua"].append("AquaVita")
        self.reactions["AquaVita"].append("PhilosopherStone")
        self.reactions["AquaVita"].append("Argentum")
        self.reactions["Argentum"].append("Aurum")
        self.reactions["AquaVita"].append("Aurum")

    def test_basic_conversion(self):
        # Проверяем простой случай, где путь существует и минимальное количество реакций
        result = alchemy_reactions(5, self.reactions, "Aqua", "Aurum")
        self.assertEqual(result, 2)  # Ожидаем минимальное количество шагов 2

    def test_direct_conversion(self):
        # Проверка случая, когда можно пройти только одну реакцию
        self.reactions = defaultdict(list)
        self.reactions["Aqua"].append("AquaVita")
        result = alchemy_reactions(1, self.reactions, "Aqua", "AquaVita")
        self.assertEqual(result, 1)  # Ожидаем 1 шаг

    def test_no_conversion_possible(self):
        # Проверяем случай, когда путь невозможен
        self.reactions = defaultdict(list)
        self.reactions["Aqua"].append("AquaVita")
        result = alchemy_reactions(1, self.reactions, "Aqua", "PhilosopherStone")
        self.assertEqual(result, -1)  # Путь не существует, ожидаем -1

    def test_no_reactions(self):
        # Проверяем случай без реакций
        self.reactions = defaultdict(list)
        result = alchemy_reactions(0, self.reactions, "Aqua", "Aurum")
        self.assertEqual(result, -1)  # Путь невозможен, так как нет реакций

    def test_same_substance(self):
        # Проверка случая, когда начальное вещество равно требуемому
        result = alchemy_reactions(5, self.reactions, "Aqua", "Aqua")
        self.assertEqual(result, 0)  # Путь не требуется, так как вещества одинаковые


if __name__ == "__main__":
    unittest.main()
