from collections import Counter
from itertools import combinations


def count_palindromic_triplets(message: str) -> int:
    # Удаляем пробелы из строки
    filtered_message = message.replace(" ", "")
    n = len(filtered_message)

    # Подсчитываем все возможные палиндромные тройки
    count = 0
    for i, j, k in combinations(range(n), 3):
        if filtered_message[i] == filtered_message[k]:
            count += 1

    return count


def read_input(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.readline().strip()


def write_output(filename: str, result: int):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(result) + "\n")


if __name__ == "__main__":
    input_text = read_input("../txtf/input.txt")
    result = count_palindromic_triplets(input_text)
    write_output("../txtf/output.txt", result)