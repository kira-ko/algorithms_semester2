import unittest
from lab2.task5.src.main import BST


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        """Создаём дерево перед каждым тестом"""
        self.bst = BST()

    def test_insert_and_exists(self):
        """Проверка вставки и существования элементов"""
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.insert(8)
        self.assertTrue(self.bst.exists(5))
        self.assertTrue(self.bst.exists(2))
        self.assertTrue(self.bst.exists(8))
        self.assertFalse(self.bst.exists(10))

    def test_delete(self):
        """Проверка удаления элементов"""
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertTrue(self.bst.exists(2))
        self.assertTrue(self.bst.exists(8))

    def test_next(self):
        """Проверка поиска следующего элемента"""
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(10)
        self.assertEqual(self.bst.next(2), 5)
        self.assertEqual(self.bst.next(5), 8)
        self.assertEqual(self.bst.next(8), 10)
        self.assertEqual(self.bst.next(10), None)

    def test_prev(self):
        """Проверка поиска предыдущего элемента"""
        self.bst.insert(5)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(1)
        self.assertEqual(self.bst.prev(8), 5)
        self.assertEqual(self.bst.prev(5), 2)
        self.assertEqual(self.bst.prev(2), 1)
        self.assertEqual(self.bst.prev(1), None)

    def test_complex_operations(self):
        """Комплексный тест на вставку, удаление, next и prev"""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertEqual(self.bst.next(3), 7)
        self.assertEqual(self.bst.prev(7), 3)
        self.assertEqual(self.bst.next(10), 15)
        self.assertEqual(self.bst.prev(15), 10)


if __name__ == "__main__":
    unittest.main()
