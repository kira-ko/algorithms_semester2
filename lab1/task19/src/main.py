

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1  #количество матриц
    dp = [[0] * n for _ in range(n)]  #массив для хранения минимальных операций
    s = [[0] * n for _ in range(n)]  #массив для хранения мест разделения (где ставить скобки)


    for length in range(2, n + 1):  #длина цепочки матриц от 2 до n
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
                    s[i][j] = k

    #рекурсивная функция для построения скобочной структуры
    def build_order(s, i, j):
        if i == j:
            return 'A'  #вывод только букв А
            # return chr(ord('A') + i)  #обозначение каждой матрици своей буквой
        k = s[i][j]
        left = build_order(s, i, k)
        right = build_order(s, k + 1, j)
        return f"({left}{right})"  #скобки вокруг левого и правого подвыражений

    return build_order(s, 0, n - 1)


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        n = int(file.readline().strip())
        dimensions = []
        for i in range(n):
            ai, bi = map(int, file.readline().split())
            dimensions.append(ai)
        dimensions.append(bi)

    result = matrix_chain_order(dimensions)

    with open("../txtf/output.txt", "w") as file:
        file.write(result)

