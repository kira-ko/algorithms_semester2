MOD = 1000000000

def horse(n):
    dp = [[0] * (n + 1) for _ in range(10)]  #инициализация массива dp
    for i in range(10):
        dp[i][1] = 1  #для длины 1

    #заполнение массива dp для всех длин от 2 до n
    for j in range(2, n + 1):
        for i in range(10):
            if i == 0:
                dp[0][j] = (dp[4][j - 1] + dp[6][j - 1]) % MOD
            elif i == 1:
                dp[1][j] = (dp[6][j - 1] + dp[8][j - 1]) % MOD
            elif i == 2:
                dp[2][j] = (dp[9][j - 1] + dp[7][j - 1]) % MOD
            elif i == 3:
                dp[3][j] = (dp[8][j - 1] + dp[4][j - 1]) % MOD
            elif i == 4:
                dp[4][j] = (dp[0][j - 1] + dp[3][j - 1] + dp[9][j - 1]) % MOD
            elif i == 6:
                dp[6][j] = (dp[0][j - 1] + dp[1][j - 1] + dp[7][j - 1]) % MOD
            elif i == 7:
                dp[7][j] = (dp[6][j - 1] + dp[2][j - 1]) % MOD
            elif i == 8:
                dp[8][j] = (dp[1][j - 1] + dp[3][j - 1]) % MOD
            elif i == 9:
                dp[9][j] = (dp[2][j - 1] + dp[4][j - 1]) % MOD

    #подсчитываем сумму всех возможных номеров длины n
    result = 0
    for i in range(1, 10):
        if i != 8:  # Исключаем 8
            result = (result + dp[i][n]) % MOD

    return result

if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        n = int(file.readline().strip())

    result = horse(n)

    with open("../txtf/output.txt", "w") as file:
        file.write(str(result))
