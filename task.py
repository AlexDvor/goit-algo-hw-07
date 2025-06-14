class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)


# Завдання 1: Знайти найбільше значення у дереві


def find_max(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.key


# Завдання 2: Знайти найменше значення у дереві


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key


#  Завдання 3: Знайти суму всіх значень у дереві


def sum_values(node):
    if node is None:
        return 0
    return node.key + sum_values(node.left) + sum_values(node.right)


if __name__ == "__main__":
    tree = BinarySearchTree()
    for value in [20, 10, 5, 15, 30, 25, 35]:
        tree.insert(value)

    print("Максимальне значення в дереві:", find_max(tree.root))
    print("Мінімальне значення в дереві:", find_min(tree.root))
    print("Сума всіх значень в дереві:", sum_values(tree.root))
