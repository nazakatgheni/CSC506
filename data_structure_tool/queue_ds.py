"""
Queue Data Structure Implementation
This class implements a queue using a Python list.
Operations:
- enqueue: O(1)
- dequeue: O(1)
Queue follows First In First Out (FIFO) principle.
"""

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0