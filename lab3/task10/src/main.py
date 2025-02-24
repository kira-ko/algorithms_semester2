def bellman_ford(n, m, edges, start):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    # Релаксация рёбер (n - 1 раз)
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Проверяем, какие вершины находятся в отрицательных циклах
    for _ in range(n):  # Делаем n итераций, чтобы все вершины из отрицательных циклов получили -inf
        for u, v, weight in edges:
            if dist[u] == -INF or (dist[u] != INF and dist[u] + weight < dist[v]):
                dist[v] = -INF  # Помечаем вершину как "участник отрицательного цикла"

    return dist


if __name__ == "__main__":
    # Читаем входные данные
    with open("../txtf/input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        edges = []
        for _ in range(m):
            u, v, weight = map(int, file.readline().split())
            edges.append((u, v, weight))
        s = int(file.readline())  # Начальная вершина

    # Вызываем алгоритм Беллмана-Форда
    dist = bellman_ford(n, m, edges, s)

    # Записываем результат в файл
    with open("../txtf/output.txt", "w") as file:
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                file.write("*\n")  # Нет пути
            elif dist[i] == -float('inf'):
                file.write("-\n")  # Отрицательный цикл
            else:
                file.write(f"{dist[i]}\n")  # Кратчайшее расстояние
