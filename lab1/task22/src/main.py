def cute_patterns(x, y, n):
    '''Функция проверяет можно ли разместить плитки
    на текущие строки (x, y): нигде не должно быть 2x2 одного цвета
    '''

    b = [0] * 5  #Вспомогательный массив для хранения значений плиток

    for i in range(n - 1):
        #Определяем цвета плиток в текущем и следующем столбцах для двух строк
        b[1] = 0 if (x & (1 << i)) == 0 else 1
        b[2] = 0 if (x & (1 << (i + 1))) == 0 else 1
        b[3] = 0 if (y & (1 << i)) == 0 else 1
        b[4] = 0 if (y & (1 << (i + 1))) == 0 else 1

        #Если четыре плитки образуют квадрат одного цвета то False
        if b[1] == b[2] == b[3] == b[4]:
            return False

    return True

def cute_patterns_main(n, m):
    '''Основная функция для подсчета количества возможных узоров'''
    res = 0
    length = 1 << n  #Количество возможных строк (2^n)
    #Возможные переходы
    a = [[0] * length for _ in range(m)]  #Количество допустимых узоров на каждом шаге
    dp = [[0] * length for _ in range(length)]  #Матрица допустимых переходов между строками

    #Заполняем dp: можно ли переходить между строками i и j
    for i in range(length):
        for j in range(length):
            dp[i][j] = 1 if cute_patterns(i, j, n) else 0

    #Инициализируем базовый случай: первая строка может быть любой
    for i in range(length):
        a[0][i] = 1

    #Заполняем массив a
    for x in range(1, m):
        for i in range(length):
            for j in range(length):
                a[x][i] += a[x - 1][j] * dp[j][i]

    for i in range(length):
        res += a[m - 1][i]

    return res

if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as f:
        n, m = map(int, f.readline().split())

    if n > m:
        n, m = m, n

    result = cute_patterns_main(n, m)

    with open("../txtf/output.txt", "w") as f:
        f.write(str(result))
