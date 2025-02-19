class Node:
    def __init__(self, key, char):
        self.key = key # Индекс символа
        self.char = char # Символ строки
        self.left = None # Правый ребенок
        self.right = None #Левый ребенок
        self.parent = None # Родитель
        self.size = 1  # Размер поддерева

class SplayTree:
    """Реализация Splay-дерева"""
    def __init__(self, s):
        """Создается дерево из строки s"""
        self.root = None
        self.build_tree(s)

    def build_tree(self, s):
        """Построение дерева из строки"""
        for i, char in enumerate(s):
            self.root = self.insert(self.root, i, char) # Вставляем символ

    def update_size(self, node):
        """Обновляет размер поддерева"""
        if node:
            node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)
        return node

    def rotate(self, node):
        """Выполняет вращение узла"""
        parent = node.parent
        grandparent = parent.parent # Дедушка
        if parent.left == node: # Малый правый поворот
            parent.left = node.right
            if node.right:
                node.right.parent = parent
            node.right = parent
        else: # Малый левый поворот
            parent.right = node.left
            if node.left:
                node.left.parent = parent
            node.left = parent
        parent.parent = node
        node.parent = grandparent

        if grandparent:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            self.root = node # Новый корень

        self.update_size(parent)
        self.update_size(node)

    def splay(self, node):
        """Балансировка дерева. Поднимает node в корень"""
        while node.parent:
            if not node.parent.parent:
                self.rotate(node)
            elif (node.parent.left == node) == (node.parent.parent.left == node.parent):
                self.rotate(node.parent) # Двойное вращение
                self.rotate(node)
            else:
                self.rotate(node) # Двойное вращение
                self.rotate(node)

    def find(self, root, index):
        """Находит узел по индексу"""
        if not root:
            return None
        left_size = root.left.size if root.left else 0
        if index < left_size:
            return self.find(root.left, index)
        elif index > left_size:
            return self.find(root.right, index - left_size - 1)
        else:
            return root # Найден нужный узел

    def split(self, root, index):
        """Разбивает дерево по индексу"""
        if not root:
            return None, None
        node = self.find(root, index)
        if not node:
            return root, None
        self.splay(node) # Поднимаем узел к корню

        left_subtree = node.left
        if left_subtree:
            left_subtree.parent = None
        node.left = None
        self.update_size(node)

        return left_subtree, node

    def merge(self, left, right):
        """Объединяет два дерева"""
        if not left:
            return right
        if not right:
            return left

        max_left = left
        while max_left.right:
            max_left = max_left.right

        self.splay(max_left) # Поднимаем максимальный узел
        max_left.right = right
        right.parent = max_left
        return self.update_size(max_left)

    def insert(self, root, index, char):
        """Вставляет символ в дерево"""
        if not root:
            return Node(index, char)
        left, right = self.split(root, index)
        new_node = Node(index, char)
        return self.merge(self.merge(left, new_node), right)

    def extract_substring(self, i, j):
        """Вырезает подстроку"""
        left, mid = self.split(self.root, i)
        mid, right = self.split(mid, j - i + 1)
        self.root = self.merge(left, right)
        return mid

    def insert_substring(self, substring, k):
        """Вставляет подстроку на позицию k"""
        left, right = self.split(self.root, k)
        self.root = self.merge(self.merge(left, substring), right)

    def inorder(self, node):
        """Обход дерева для получения строки"""
        if not node:
            return ""
        return self.inorder(node.left) + node.char + self.inorder(node.right)

    def get_string(self):
        """Возвращает строку из дерева"""
        return self.inorder(self.root)

def process_queries(s, queries):
    """Обрабатывает запросы"""
    tree = SplayTree(s)
    for i, j, k in queries:
        substring = tree.extract_substring(i, j)
        tree.insert_substring(substring, k)
    return tree.get_string()

def main():
    with open("../txtf/input.txt", "r") as f:
        s = f.readline().strip()
        n = int(f.readline().strip())
        queries = [tuple(map(int, f.readline().split())) for _ in range(n)]

    result = process_queries(s, queries)

    with open("../txtf/output.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()
