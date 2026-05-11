class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack


if __name__ == "__main__":
    order_history = Stack()

    order_history.push("Order #1001")
    order_history.push("Order #1002")

    print(order_history.display())
    print("Removed:", order_history.pop())
    print(order_history.display())
    