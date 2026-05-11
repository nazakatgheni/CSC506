from tkinter import *
from tkinter import messagebox

from bubble_sort import BubbleSort
from quickselect import QuickSelect
from set_class import CustomSet
from stack import Stack
from queue_ds import Queue
from bst import BinarySearchTree
from graph import Graph
from hash_table import HashTable


class PortfolioUI:

    def __init__(self, root):

        self.root = root
        self.root.title("CSC506 Portfolio Project")
        self.root.geometry("900x700")
        self.root.configure(bg="#f4f4f4")

        title = Label(
            root,
            text="Home Depot Order Tracking & Management System",
            font=("Arial", 20, "bold"),
            fg="#333",
            bg="#f4f4f4",
        )

        title.pack(pady=15)

        button_frame = Frame(root, bg="#f4f4f4")
        button_frame.pack(pady=10)

        Button(
            button_frame,
            text="Bubble Sort",
            width=20,
            command=self.run_bubble_sort
        ).grid(row=0, column=0, padx=5, pady=5)

        Button(
            button_frame,
            text="Quickselect",
            width=20,
            command=self.run_quickselect
        ).grid(row=0, column=1, padx=5, pady=5)

        Button(
            button_frame,
            text="Set Operations",
            width=20,
            command=self.run_set_operations
        ).grid(row=1, column=0, padx=5, pady=5)

        Button(
            button_frame,
            text="Stack Demo",
            width=20,
            command=self.run_stack_demo
        ).grid(row=1, column=1, padx=5, pady=5)

        Button(
            button_frame,
            text="Queue Demo",
            width=20,
            command=self.run_queue_demo
        ).grid(row=2, column=0, padx=5, pady=5)

        Button(
            button_frame,
            text="BST Demo",
            width=20,
            command=self.run_bst_demo
        ).grid(row=2, column=1, padx=5, pady=5)

        Button(
            button_frame,
            text="Graph Demo",
            width=20,
            command=self.run_graph_demo
        ).grid(row=3, column=0, padx=5, pady=5)

        Button(
            button_frame,
            text="Hash Table Demo",
            width=20,
            command=self.run_hash_demo
        ).grid(row=3, column=1, padx=5, pady=5)

        Button(
            button_frame,
            text="Clear Output",
            width=20,
            command=self.clear_output
        ).grid(row=4, column=0, columnspan=2, pady=10)

        self.output = Text(
            root,
            width=100,
            height=25,
            font=("Courier", 11)
        )

        self.output.pack(pady=15)

    def clear_output(self):
        self.output.delete(1.0, END)

    def run_bubble_sort(self):

        self.clear_output()

        numbers = [64, 34, 25, 12, 22, 11, 90]

        sorted_numbers, steps = BubbleSort.sort(numbers)

        self.output.insert(
            END,
            "=== Bubble Sort Visualization ===\n\n"
        )

        self.output.insert(
            END,
            f"Original List: {numbers}\n\n"
        )

        for step in steps:
            self.output.insert(END, step + "\n")

        self.output.insert(
            END,
            f"\nFinal Sorted List: {sorted_numbers}"
        )

    def run_quickselect(self):

        self.clear_output()

        numbers = [7, 10, 4, 3, 20, 15]
        k = 2

        result = QuickSelect.quickselect(numbers, k)

        self.output.insert(
            END,
            "=== Quickselect Algorithm ===\n\n"
        )

        self.output.insert(
            END,
            f"Numbers: {numbers}\n"
        )

        self.output.insert(
            END,
            f"{k + 1}rd smallest element is: {result}\n"
        )

    def run_set_operations(self):

        self.clear_output()

        warehouse_a = CustomSet()
        warehouse_b = CustomSet()

        for item in ["Hammer", "Drill", "Saw"]:
            warehouse_a.add(item)

        for item in ["Saw", "Ladder", "Drill"]:
            warehouse_b.add(item)

        self.output.insert(
            END,
            "=== Set Operations ===\n\n"
        )

        self.output.insert(
            END,
            f"Warehouse A: {warehouse_a.display()}\n"
        )

        self.output.insert(
            END,
            f"Warehouse B: {warehouse_b.display()}\n\n"
        )

        self.output.insert(
            END,
            f"Union: {warehouse_a.union(warehouse_b).display()}\n"
        )

        self.output.insert(
            END,
            f"Intersection: {warehouse_a.intersection(warehouse_b).display()}\n"
        )

        self.output.insert(
            END,
            f"Difference: {warehouse_a.difference(warehouse_b).display()}\n"
        )

        self.output.insert(
            END,
            "Symmetric Difference: "
            f"{warehouse_a.symmetric_difference(warehouse_b).display()}\n"
        )

    def run_stack_demo(self):

        self.clear_output()

        order_stack = Stack()

        order_stack.push("Order #1001")
        order_stack.push("Order #1002")
        order_stack.push("Order #1003")

        removed = order_stack.pop()

        self.output.insert(
            END,
            "=== Stack Demo ===\n\n"
        )

        self.output.insert(
            END,
            "Stacks use LIFO (Last In First Out)\n\n"
        )

        self.output.insert(
            END,
            f"Removed Order: {removed}\n"
        )

        self.output.insert(
            END,
            f"Current Stack: {order_stack.display()}\n"
        )

    def run_queue_demo(self):

        self.clear_output()

        shipping_queue = Queue()

        shipping_queue.enqueue("Customer A")
        shipping_queue.enqueue("Customer B")
        shipping_queue.enqueue("Customer C")

        processed = shipping_queue.dequeue()

        self.output.insert(
            END,
            "=== Queue Demo ===\n\n"
        )

        self.output.insert(
            END,
            "Queues use FIFO (First In First Out)\n\n"
        )

        self.output.insert(
            END,
            f"Processed Customer: {processed}\n"
        )

        self.output.insert(
            END,
            f"Current Queue: {shipping_queue.display()}\n"
        )

    def run_bst_demo(self):

        self.clear_output()

        bst = BinarySearchTree()

        bst.insert(1001, "Nazakat")
        bst.insert(1002, "Sarah")
        bst.insert(1003, "John")

        search_result = bst.search(1002)

        self.output.insert(
            END,
            "=== Binary Search Tree Demo ===\n\n"
        )

        self.output.insert(
            END,
            "Searching for Order #1002...\n\n"
        )

        self.output.insert(
            END,
            f"Customer Found: {search_result}\n"
        )

    def run_graph_demo(self):

        self.clear_output()

        delivery_graph = Graph()

        delivery_graph.add_vertex("Warehouse")
        delivery_graph.add_vertex("Store")
        delivery_graph.add_vertex("Customer")

        delivery_graph.add_edge("Warehouse", "Store")
        delivery_graph.add_edge("Store", "Customer")

        self.output.insert(
            END,
            "=== Graph Demo ===\n\n"
        )

        self.output.insert(
            END,
            "Delivery Route Connections:\n\n"
        )

        self.output.insert(
            END,
            str(delivery_graph.display())
        )

    def run_hash_demo(self):

        self.clear_output()

        orders = HashTable()

        orders.insert(1001, "Nazakat")
        orders.insert(1002, "Sarah")
        orders.insert(1003, "John")

        customer = orders.search(1002)

        self.output.insert(
            END,
            "=== Hash Table Demo ===\n\n"
        )

        self.output.insert(
            END,
            "Fast Order Lookup Using Hash Table\n\n"
        )

        self.output.insert(
            END,
            f"Order #1002 belongs to: {customer}\n"
        )


if __name__ == "__main__":

    root = Tk()

    app = PortfolioUI(root)

    root.mainloop()