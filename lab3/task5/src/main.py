# Алгоритм для нахождения количества компонентов сильной связности
def one_way_city(n, adj):
    """Реализация алгоритма Тарьяна для нахождения компонент сильной связности"""
    index = [None] * n  # Массив индексов для каждой вершины
    lowlink = [None] * n  # Массив lowlink для каждой вершины
    on_stack = [False] * n  # Массив для отслеживания, находится ли вершина в стеке
    stack = []  # Стек для хранения вершин
    scc_count = 0  # Счётчик компонентов сильной связности
    current_index = 0  # Индекс для присвоения вершинам

    def strongconnect(v):
        nonlocal current_index, scc_count

        # Присваиваем вершине индекс и lowlink
        index[v] = current_index
        lowlink[v] = current_index
        current_index += 1
        stack.append(v)
        on_stack[v] = True

        # Проходим по всем соседям вершины v
        for w in adj[v]:
            if index[w] is None:
                # Если сосед ещё не был посещён, рекурсивно вызываем strongconnect
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                # Если сосед в стеке, обновляем lowlink
                lowlink[v] = min(lowlink[v], index[w])

        # Если вершина v является корнем компоненты сильной связности
        if lowlink[v] == index[v]:
            # Формируем компоненту сильной связности
            scc_count += 1
            while True:
                w = stack.pop()
                on_stack[w] = False
                if w == v:
                    break

    # Запускаем алгоритм для каждой вершины
    for v in range(n):
        if index[v] is None:
            strongconnect(v)

    return scc_count


# Основная программа
if __name__ == "__main__":
    with open('../txtf/input.txt', 'r') as file:
        n, m = map(int, file.readline().split())  # Читаем количество вершин и рёбер
        adj = [[] for _ in range(n)]  # Список смежности
        for _ in range(m):
            u, v = map(int, file.readline().split())  # Читаем рёбра
            adj[u - 1].append(v - 1)  # Добавляем ребро в список смежности

    # Решаем задачу
    result = tarjan_scc(n, adj)

    # Запись результата в файл
    with open('../txtf/output.txt', 'w') as file:
        file.write(f"{result}\n")
