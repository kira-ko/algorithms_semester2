def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


if __name__ == "__main__":
    # Чтение входных данных
    with open("../txtf/input.txt", "r") as f:
        s = f.readline().strip()

    # Вычисление префикс-функции
    prefix_values = compute_prefix_function(s)

    # Запись результата в файл
    with open("../txtf/output.txt", "w") as f:
        f.write(" ".join(map(str, prefix_values)) + "\n")