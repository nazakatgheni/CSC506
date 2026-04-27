from bst import BST

class BSTMap:
    def __init__(self):
        self.tree = BST()

    def put(self, key, value):
        self.tree.insert(key, value)

    def get(self, key):
        return self.tree.search(key)

    def remove(self, key):
        self.tree.delete(key)

    def min(self):
        return self.tree.find_min()

    def max(self):
        return self.tree.find_max()

    def is_balanced(self):
        return self.tree.is_balanced()

    def inorder(self):
        return self.tree.inorder()