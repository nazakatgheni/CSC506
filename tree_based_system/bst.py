class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # update existing

        return node

    # SEARCH
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None

        if key == node.key:
            return node.value

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # FIND MIN
    def find_min(self):
        node = self._find_min(self.root)
        return (node.key, node.value) if node else None

    def _find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    # FIND MAX
    def find_max(self):
        node = self._find_max(self.root)
        return (node.key, node.value) if node else None

    def _find_max(self, node):
        while node and node.right:
            node = node.right
        return node

    # DELETE
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # case 1: no child
            if node.left is None and node.right is None:
                return None

            # case 2: one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # case 3: two children
            min_larger_node = self._find_min(node.right)
            node.key, node.value = min_larger_node.key, min_larger_node.value
            node.right = self._delete(node.right, min_larger_node.key)

        return node

    # TRAVERSALS
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append((node.key, node.value))
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append((node.key, node.value))
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append((node.key, node.value))

    # HEIGHT
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # BALANCE CHECK
    def is_balanced(self):
        return self._is_balanced(self.root)

    def _is_balanced(self, node):
        if node is None:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)

    # PRINT TREE (visual)
    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self.print_tree(node.left, level + 1)