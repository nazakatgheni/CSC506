"""
Linear Data Structures Implementation
Includes Stack, Queue, Deque, and Singly Linked List.
"""

class Stack:
    """A Stack implementation using a Python list (LIFO)."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")

class Queue:
    """A Queue implementation using a Python list (FIFO)."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("Dequeue from empty queue")

    def front(self):
        if not self.isEmpty():
            return self.items[-1]
        raise IndexError("Front from empty queue")

class Deque:
    """A Double-Ended Queue using a Python list."""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("Remove from empty deque")

    def removeRear(self):
        if not self.isEmpty():
            return self.items.pop(0)
        raise IndexError("Remove from empty deque")

class Node:
    """Node class for the LinkedList."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly Linked List implementation."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Appends a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Deletes the first occurrence of the specified key."""
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return True
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
            
        if current is None:
            return False
            
        prev.next = current.next
        return True

    def search(self, key):
        """Searches for a key and returns a boolean."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Returns list elements as a Python list for easy viewing."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements