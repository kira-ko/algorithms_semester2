def min_print(N, A):
    batch_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]  # Размеры партий
    min_cost = float('inf')  # Изначально бесконечная стоимость

    # Перебираем все доступные тарифы
    for i in range(7):
        batch_size = batch_sizes[i]
        batch_cost = A[i]

        # Определяем необходимое количество партий
        num_batches = (N + batch_size - 1) // batch_size
        total_cost = num_batches * batch_cost

        # Обновляем минимальную стоимость
        min_cost = min(min_cost, total_cost)

    return min_cost



if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        N = int(file.readline().strip())
        A = [int(file.readline().strip()) for _ in range(7)]

    result = min_print(N, A)

    with open("../txtf/output.txt", "w") as file:
        file.write(str(result) + "\n")