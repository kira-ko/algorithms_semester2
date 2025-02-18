def remove_invalid_brackets(s: str) -> str:
    stack = []
    to_remove = set()

    for i, char in enumerate(s):
        if char in '([{':
            stack.append((char, i))  # добавляем в стек с индексом
        elif char in ')]}':
            if stack and ((char == ')' and stack[-1][0] == '(') or
                          (char == ']' and stack[-1][0] == '[') or
                          (char == '}' and stack[-1][0] == '{')):
                stack.pop()  # находим пару, убираем из стека
            else:
                to_remove.add(i)  # добавляем в список на удаление

    # Добавляем оставшиеся символы из стека
    to_remove.update(i for _, i in stack)

    return ''.join(char for i, char in enumerate(s) if i not in to_remove)


if __name__ == "__main__":
    with open("../txtf/input.txt", "r") as file:
        s = file.readline().strip()

    result = remove_invalid_brackets(s)

    with open("../txtf/output.txt", "w") as file:
        file.write(result + "\n")
