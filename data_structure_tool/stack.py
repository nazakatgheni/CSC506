"""
Stack Data Structure Implementation
This class implements a stack using a Python list.
Operations:
- push: O(1)
- pop: O(1)
- peek: O(1)
Stack follows Last In First Out (LIFO) principle.
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0