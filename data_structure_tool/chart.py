import matplotlib.pyplot as plt
from performance import test_stack, test_queue, test_linked_list

sizes = [100, 1000, 5000, 10000]

stack_times = []
queue_times = []
linked_times = []

for n in sizes:
    stack_times.append(test_stack(n))
    queue_times.append(test_queue(n))
    linked_times.append(test_linked_list(n))

plt.plot(sizes, stack_times, label="Stack Push O(1)")
plt.plot(sizes, queue_times, label="Queue Enqueue O(1)")
plt.plot(sizes, linked_times, label="Linked List Search O(n)")

plt.xlabel("Number of Elements")
plt.ylabel("Execution Time")
plt.title("Performance Comparison of Data Structures")
plt.legend()

plt.show()