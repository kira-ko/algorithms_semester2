import unittest
from lab3.task5.src.main import one_way_city

def parse_input(input_data):
    """Парсинг входных данных в формат для алгоритма"""
    lines = input_data.strip().split('\n')
    n, m = map(int, lines[0].split())
    adj = [[] for _ in range(n)]
    for line in lines[1:]:
        u, v = map(int, line.split())
        adj[u - 1].append(v - 1)  # Входим в 0-индексацию
    return n, adj


class TestSCC(unittest.TestCase):

    def test_graph_with_two_scc(self):
        input_data = """4 4
        1 2
        4 1
        2 3
        3 1"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 2)

    def test_empty_graph(self):
        input_data = """3 0"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 3)

    def test_single_component(self):
        input_data = """3 3
        1 2
        2 3
        3 1"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 1)

    def test_disconnected_graph(self):
        input_data = """4 4
        1 2
        2 1
        3 4
        4 3"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 2)

    def test_single_vertex(self):
        input_data = """1 0"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 1)

    def test_graph_with_cycle(self):
        input_data = """4 4
        1 2
        2 3
        3 4
        4 1"""
        n, adj = parse_input(input_data)
        self.assertEqual(one_way_city(n, adj), 1)


if __name__ == '__main__':
    unittest.main()

