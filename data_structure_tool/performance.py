import time
from stack import Stack
from queue_ds import Queue
from linked_list import LinkedList

def test_stack(n):
    s = Stack()
    start = time.time()
    for i in range(n):
        s.push(i)
    end = time.time()
    return end - start

def test_queue(n):
    q = Queue()
    start = time.time()
    for i in range(n):
        q.enqueue(i)
    end = time.time()
    return end - start

def test_linked_list(n):
    ll = LinkedList()
    for i in range(n):
        ll.insert(i)

    start = time.time()
    for _ in range(1000):
        ll.search(n-1)
    end = time.time()
    return end - start

def run_tests():
    sizes = [100, 1000, 5000, 10000]

    for n in sizes:
        print("Size:", n)
        print("Stack push time:", test_stack(n))
        print("Queue enqueue time:", test_queue(n))
        print("Linked list search time:", test_linked_list(n))
        print()