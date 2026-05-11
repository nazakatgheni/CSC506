class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return self.queue


if __name__ == "__main__":
    shipping_queue = Queue()

    shipping_queue.enqueue("Customer A")
    shipping_queue.enqueue("Customer B")

    print(shipping_queue.display())
    print("Processed:", shipping_queue.dequeue())
    print(shipping_queue.display())