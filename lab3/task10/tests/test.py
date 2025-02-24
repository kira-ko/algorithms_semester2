import unittest
from lab3.task10.src.main import bellman_ford

class TestBellmanFord(unittest.TestCase):
    def test_simple_case(self):
        """Тест для графа без отрицательных рёбер"""
        n, m = 3, 3
        edges = [
            (1, 2, 4),
            (2, 3, -6),
            (1, 3, 2)
        ]
        s = 1
        expected_output = [float('inf'), 0, 4, -2]  # dist[0] игнорируется
        self.assertEqual(bellman_ford(n, m, edges, s), expected_output)

    def test_no_path(self):
        """Тест, где нет пути до некоторых вершин"""
        n, m = 4, 2
        edges = [
            (1, 2, 3),
            (2, 3, 5)
        ]
        s = 1
        expected_output = [float('inf'), 0, 3, 8, float('inf')]
        self.assertEqual(bellman_ford(n, m, edges, s), expected_output)

    def test_negative_cycle(self):
        """Тест с отрицательным циклом"""
        n, m = 4, 4
        edges = [
            (1, 2, 1),
            (2, 3, 1),
            (3, 4, -3),
            (4, 2, 1)
        ]
        s = 1
        expected_output = [float('inf'), 0, -float('inf'), -float('inf'), -float('inf')]
        self.assertEqual(bellman_ford(n, m, edges, s), expected_output)

    def test_disconnected_graph(self):
        """Тест с вершиной, которая не соединена с другими"""
        n, m = 5, 3
        edges = [
            (1, 2, 10),
            (2, 3, 5),
            (3, 4, -2)
        ]
        s = 1
        expected_output = [float('inf'), 0, 10, 15, 13, float('inf')]
        self.assertEqual(bellman_ford(n, m, edges, s), expected_output)

    def test_single_node(self):
        """Тест для графа с одной вершиной"""
        n, m = 1, 0
        edges = []
        s = 1
        expected_output = [float('inf'), 0]  # Только одна вершина, расстояние до неё 0
        self.assertEqual(bellman_ford(n, m, edges, s), expected_output)

if __name__ == "__main__":
    unittest.main()
