import heapq

def dijkstra(n, adj, start, end):
    # Инициализация расстояний до всех вершин как бесконечность
    dist = [float('inf')] * n
    dist[start] = 0

    # Очередь с приоритетами (min-heap)
    pq = [(0, start)]  # (расстояние, вершина)

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Если текущий путь уже длиннее найденного, пропускаем его
        if current_dist > dist[u]:
            continue

        # Обрабатываем все рёбра из вершины u
        for v, weight in adj[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    # Возвращаем минимальное расстояние до вершины end, если оно существует
    return dist[end] if dist[end] != float('inf') else -1



if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        n, m = map(int, file.readline().split())  # количество вершин и рёбер
        adj = [[] for _ in range(n)]

        # Строим граф
        for _ in range(m):
            u, v, weight = map(int, file.readline().split())
            adj[u - 1].append((v - 1, weight))  # смещаем на 0-индексацию
        # Чтение начальной и конечной вершины
        start, end = map(int, file.readline().split())

    result = dijkstra(n, adj, start - 1, end - 1)  # смещаем на 0-индексацию

    with open("../txtf/output.txt", "w") as file:
        file.write(str(result) + "\n")
