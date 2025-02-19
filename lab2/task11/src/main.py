class AVLTreeNode:
    def __init__(self, key):
        """Инициализация узла AVL-дерева"""
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        """Инициализация пустого AVL-дерева"""
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        """Правый поворот вокруг узла y"""
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        return x

    def _rotate_left(self, x):
        """Левый поворот вокруг узла x"""
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        return y

    def _balance(self, node):
        """Балансировка узла"""
        if not node:
            return node

        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert(self, node, key):
        """Рекурсивное добавление ключа в дерево"""
        if not node:
            return AVLTreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self._balance(node)

    def insert(self, key):
        """Обёртка для публичного вызова insert"""
        self.root = self._insert(self.root, key)

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        """Рекурсивное удаление узла"""
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return self._balance(node)

    def delete(self, key):
        """Удаление узла по ключу"""
        self.root = self._delete(self.root, key)

    def exists(self, key):
        """Проверка существования ключа в дереве"""
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return True
        return False

    def next(self, key):
        """Поиск минимального элемента строго больше key"""
        node, successor = self.root, None
        while node:
            if node.key > key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.key if successor else "none"

    def prev(self, key):
        """Поиск максимального элемента строго меньше key"""
        node, predecessor = self.root, None
        while node:
            if node.key < key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.key if predecessor else "none"


def process_operations(input_file, output_file):
    """Читает команды из input.txt, выполняет их и записывает результат в output.txt"""
    tree = AVLTree()
    results = []

    with open(input_file, 'r') as f:
        for line in f:
            parts = line.split()
            command, x = parts[0], int(parts[1])

            if command == "insert":
                tree.insert(x)
            elif command == "delete":
                tree.delete(x)
            elif command == "exists":
                results.append("true" if tree.exists(x) else "false")
            elif command == "next":
                results.append(str(tree.next(x)))
            elif command == "prev":
                results.append(str(tree.prev(x)))

    with open(output_file, 'w') as f:
        f.write("\n".join(results) + "\n")


if __name__ == "__main__":
    process_operations("../txtf/input.txt", "../txtf/output.txt")
