import unittest
from lab2.task18.src.main import process_queries, SplayTree, Node

class TestSplayTree(unittest.TestCase):
    def setUp(self):
        """Создаёт дерево для тестов"""
        self.tree = SplayTree("hlelowrold")

    def test_find(self):
        """Тест поиска узла"""
        node = self.tree.find(self.tree.root, 2)
        self.assertIsNotNone(node)
        self.assertEqual(node.char, 'e')

    def test_split(self):
        """Тест разбиения дерева"""
        left, right = self.tree.split(self.tree.root, 5)
        self.assertIsNotNone(left)
        self.assertIsNotNone(right)
        self.assertLessEqual(left.size, 5)

    def test_process_queries(self):
        """Тест на пример из условия"""
        s = "hlelowrold"
        queries = [(1, 1, 2), (6, 6, 7)]
        result = process_queries(s, queries)
        self.assertEqual(result, "helloworld")

if __name__ == "__main__":
    unittest.main()
