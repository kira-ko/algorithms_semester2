import sys

class TreeNode:
    def __init__(self, key, left=None, right=None):
        """Создаем узел дерева с ключом и указателями на левого и правого потомка"""
        self.key = key
        self.left = left
        self.right = right

def build_tree(nodes):
    """Создает дерево из списка узлов, представленных в формате (ключ, левый_индекс, правый_индекс)"""
    if not nodes:
        return None

    tree = {i + 1: TreeNode(key) for i, (key, _, _) in enumerate(nodes)}  #Создаем узлы

    for i, (_, left, right) in enumerate(nodes):
        if left:
            tree[i + 1].left = tree[left]  #Привязываем левого потомка
        if right:
            tree[i + 1].right = tree[right]  #Привязываем правого потомка

    return tree[1]  #Корень дерева (индекс 1 всегда)


def tree_height(root):
    """Рекурсивно вычисляет высоту двоичного дерева"""
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def main():
    """Считываем данные из файла, строим дерево и вычисляем его высоту"""
    with open("../txtf/input.txt", "r") as f:
        n = int(f.readline().strip())  #количество узлов
        nodes = [tuple(map(int, f.readline().split())) for _ in range(n)]  #узлы

    root = build_tree(nodes)  #Строим дерево
    height = tree_height(root)  #Вычисляем высоту

    with open("../txtf/output.txt", "w") as f:
        f.write(str(height) + "\n")


if __name__ == "__main__":
    main()
