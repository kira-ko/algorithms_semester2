def max_expression_value(expression):
    nums = [int(expression[i]) for i in range(0, len(expression), 2)]
    ops = [expression[i] for i in range(1, len(expression), 2)]

    n = len(nums)

    #Инициализация DP таблиц
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    #Инициализация для выражений длины 1
    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    #Заполняем таблицы для всех подвыражений
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            for k in range(i, j):
                op = ops[k]
                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                elif op == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
                elif op == '*':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] * dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] * dp_min[k + 1][j])

    #Ответом будет максимальное значение на всем интервале от 0 до n-1
    return dp_max[0][n - 1]


if __name__ == '__main__':
    with open("../txtf/input.txt", "r") as file:
        expression = file.readline().strip()

    result = max_expression_value(expression)

    with open("../txtf/output.txt", "w") as file:
        file.write(str(result) + "\n")
