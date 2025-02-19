def bellman_ford(n, m, edges, start):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    # Relaxation step for n-1 times
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Detect negative weight cycles
    reachable_from_start = [False] * (n + 1)
    for _ in range(1):
        for u, v, weight in edges:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = -float('inf')
                reachable_from_start[v] = True

    return dist, reachable_from_start


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        n, m = map(int, file.readline().split())
        edges = []
        for _ in range(m):
            u, v, weight = map(int, file.readline().split())
            edges.append((u, v, weight))
        s = int(file.readline())

    dist, negative_cycle = bellman_ford(n, m, edges, s)

    # Запись результата в файл
    with open("../txtf/output.txt", "w") as file:
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                file.write("*\n")
            elif dist[i] == -float('inf') or negative_cycle[i]:
                file.write("-\n")
            else:
                file.write(f"{dist[i]}\n")
