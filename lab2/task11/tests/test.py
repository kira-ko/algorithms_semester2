import unittest
from lab2.task11.src.main import AVLTree

class TestBalancedBST(unittest.TestCase):
    def setUp(self):
        self.tree = AVLTree()

    def test_insert_and_exists(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(3)
        self.assertTrue(self.tree.exists(2))
        self.assertFalse(self.tree.exists(4))

    def test_next(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(3)
        self.assertEqual(self.tree.next(4), 5)
        self.assertEqual(self.tree.next(5), 'none')

    def test_prev(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(3)
        self.assertEqual(self.tree.prev(4), 3)
        self.assertEqual(self.tree.prev(2), 'none')

    def test_delete(self):
        self.tree.insert(2)
        self.tree.insert(5)
        self.tree.insert(3)
        self.tree.delete(5)
        self.assertEqual(self.tree.next(4), 'none')
        self.assertEqual(self.tree.prev(4), 3)

if __name__ == '__main__':
    unittest.main()