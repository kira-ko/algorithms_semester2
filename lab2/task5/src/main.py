class TreeNode:
    #Узел дерева, содержащий ключ и ссылки на левое и правое поддеревья
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    #Бинарное дерево поиска
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Вставка ключа в дерево"""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)  #Если узел пуст, создаем новый
        if key < node.key:
            node.left = self._insert(node.left, key)  #Рекурсивно вставляем в левое поддерево
        elif key > node.key:
            node.right = self._insert(node.right, key)  #Рекурсивно вставляем в правое поддерево
        return node

    def delete(self, key):
        """Удаление ключа из дерева"""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None  #Если узел пуст, ничего не делаем
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right  #Если нет левого поддерева, возвращаем правое
            if node.right is None:
                return node.left  #Если нет правого поддерева, возвращаем левое
            min_larger_node = self._min_value_node(node.right)  # Находим наименьший узел в правом поддереве
            node.key = min_larger_node.key  # Заменяем текущий узел найденным
            node.right = self._delete(node.right, min_larger_node.key)
        return node

    def _min_value_node(self, node):
        """Находит минимальный узел в поддереве"""
        while node.left is not None:
            node = node.left
        return node

    def exists(self, key):
        """Проверяет существование ключа в дереве"""
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._exists(node.left, key)
        return self._exists(node.right, key)

    def next(self, key):
        """Находит минимальный элемент, строго больший key"""
        successor = None
        node = self.root
        while node:
            if node.key > key:
                successor = node
                node = node.left
            else:
                node = node.right
        return successor.key if successor else None

    def prev(self, key):
        """Находит максимальный элемент, строго меньший key"""
        predecessor = None
        node = self.root
        while node:
            if node.key < key:
                predecessor = node
                node = node.right
            else:
                node = node.left
        return predecessor.key if predecessor else None


def main():
    """Считывает команды из input.txt и записывает результаты в output.txt"""
    bst = BST()
    with open('../txtf/input.txt', 'r') as f:
        commands = f.readlines()

    results = []
    for command in commands:
        parts = command.strip().split()
        if len(parts) != 2:
            continue
        op, x = parts[0], int(parts[1])
        if op == 'insert':
            bst.insert(x)
        elif op == 'delete':
            bst.delete(x)
        elif op == 'exists':
            results.append("true" if bst.exists(x) else "false")
        elif op == 'next':
            res = bst.next(x)
            results.append(str(res) if res is not None else "none")
        elif op == 'prev':
            res = bst.prev(x)
            results.append(str(res) if res is not None else "none")

    with open('../txtf/output.txt', 'w') as f:
        f.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()

