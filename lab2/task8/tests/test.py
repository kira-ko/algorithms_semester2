import unittest
from lab2.task8.src.main import TreeNode, tree_height, build_tree


class TestTreeHeight(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(tree_height(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(tree_height(root), 1)

    def test_balanced_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(tree_height(root), 2)

    def test_unbalanced_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)), None)
        self.assertEqual(tree_height(root), 3)

    def test_large_tree(self):
        nodes = [(1, 2, 3), (2, 4, 5), (3, 0, 0), (4, 0, 0), (5, 0, 0)]
        root = build_tree(nodes)
        self.assertEqual(tree_height(root), 3)


if __name__ == "__main__":
    unittest.main()
