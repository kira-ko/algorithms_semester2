import unittest
from lab3.task8.src.main import dijkstra


class TestDijkstra(unittest.TestCase):

    def test_shortest_path_exists(self):
        # Граф с 4 вершинами и рёбрами
        adj = [
            [(1, 1)],  # 1 - 2 (стоимость 1)
            [(2, 2)],  # 2 - 3 (стоимость 2)
            [(0, 2)],  # 3 - 1 (стоимость 2)
            []  # 4 не имеет исходящих рёбер
        ]
        n = 4
        start = 0  # Вершина 1 (с индексом 0)
        end = 2  # Вершина 3 (с индексом 2)
        result = dijkstra(n, adj, start, end)
        self.assertEqual(result, 3)  # Ожидаемый минимальный путь: 1 - 2 - 3, стоимость 3

    def test_no_path(self):
        # Граф с 4 вершинами, но без пути между вершинами 1 и 4
        adj = [
            [(1, 1)],  # 1 - 2
            [(2, 2)],  # 2 - 3
            [],  # 3 не имеет исходящих рёбер
            [(0, 2)]  # 4 - 1
        ]
        n = 4
        start = 0  # Вершина 1 (с индексом 0)
        end = 3  # Вершина 4 (с индексом 3)
        result = dijkstra(n, adj, start, end)
        self.assertEqual(result, -1)  # Путь отсутствует

    def test_multiple_edges(self):
        # Граф с несколькими рёбрами между вершинами
        adj = [
            [(1, 1), (2, 4)],  # 1 - 2 (стоимость 1), 1 - 3 (стоимость 4)
            [(2, 2)],  # 2 - 3 (стоимость 2)
            [(1, 1)],  # 3 - 2 (стоимость 1)
            []  # 4 не имеет исходящих рёбер
        ]
        n = 4
        start = 0  # Вершина 1 (с индексом 0)
        end = 2  # Вершина 3 (с индексом 2)
        result = dijkstra(n, adj, start, end)
        self.assertEqual(result, 3)  # Ожидаемый минимальный путь: 1 - 2 - 3, стоимость 3

    def test_single_edge(self):
        # Граф с одним ребром
        adj = [
            [(1, 1)],  # 1 - 2 (стоимость 1)
            []  # 2 не имеет исходящих рёбер
        ]
        n = 2
        start = 0  # Вершина 1 (с индексом 0)
        end = 1  # Вершина 2 (с индексом 1)
        result = dijkstra(n, adj, start, end)
        self.assertEqual(result, 1)  # Путь 1 - 2, стоимость 1

    def test_empty_graph(self):
        # Граф без рёбер
        adj = [[] for _ in range(5)]  # 5 вершин, но нет рёбер
        n = 5
        start = 0  # Вершина 1 (с индексом 0)
        end = 4  # Вершина 5 (с индексом 4)
        result = dijkstra(n, adj, start, end)
        self.assertEqual(result, -1)  # Путь отсутствует


if __name__ == "__main__":
    unittest.main()