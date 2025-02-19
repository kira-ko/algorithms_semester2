from collections import deque, defaultdict


def alchemy_reactions(m, reactions, start, end):
    # Если начальное вещество равно требуемому, минимальное количество реакций равно 0
    if start == end:
        return 0

    # BFS для поиска кратчайшего пути
    queue = deque([(start, 0)])  # В очередь кладем начальное вещество и счетчик шагов
    visited = set([start])  # Множество посещенных веществ

    while queue:
        current, steps = queue.popleft()

        # Перебираем все возможные реакции для текущего вещества
        for next_substance in reactions[current]:
            if next_substance == end:
                return steps + 1
            if next_substance not in visited:
                visited.add(next_substance)
                queue.append((next_substance, steps + 1))

    # Если путь не найден, возвращаем -1
    return -1


if __name__ == "__main__":
    # Чтение данных из файла
    with open('../txtf/input.txt', 'r') as f:
        m = int(f.readline().strip())  # Количество реакций
        reactions = defaultdict(list)  # Словарь для графа
        for _ in range(m):
            reaction = f.readline().strip().split(' -> ')
            reactions[reaction[0]].append(reaction[1])

        start = f.readline().strip()
        end = f.readline().strip()

    result = alchemy_reactions(m, reactions, start, end)

    with open('../txtf/output.txt', 'w') as f:
        f.write(f"{result}\n")
