class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)

        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node.value

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)


if __name__ == "__main__":
    bst = BinarySearchTree()

    bst.insert(1001, "Nazakat")
    bst.insert(1002, "John")
    bst.insert(1003, "Sarah")

    print(bst.search(1002))