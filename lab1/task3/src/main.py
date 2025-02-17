def max_revenue_calculate(a, b):
    '''вычисляет маскимальный доход от рекламы'''
    a.sort(reverse=True) #список прибыли за клик
    b.sort(reverse=True) #список среднего количества кликов
    return sum(a[i] * b[i] for i in range(len(a)))

def max_ad_revenue(input_file: str, output_file: str):
    '''читает, вычисляет и записывает данные'''
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().split()))
        b = list(map(int, f.readline().split()))

    max_revenue = max_revenue_calculate(a, b)

    with open(output_file, 'w') as f:
        f.write(str(max_revenue) + "\n")

if __name__ == "__main__":
    max_ad_revenue('../txtf/input.txt', '../txtf/output.txt')


