import random
import time
from linear_search import linear_search
from binary_search import binary_search


def generate_array(size):
    arr = random.sample(range(size * 10), size)
    return arr


def test_performance():
    sizes = [100, 1000, 10000]

    print("Performance Results")
    print("-------------------")

    for size in sizes:
        arr = generate_array(size)
        target = arr[-1]  # worst case for linear search

        # Linear Search Timing
        start = time.time()
        linear_search(arr, target)
        end = time.time()
        linear_time = end - start

        # Binary Search Timing
        arr.sort()
        start = time.time()
        binary_search(arr, target)
        end = time.time()
        binary_time = end - start

        print(f"Array Size: {size}")
        print(f"Linear Search Time: {linear_time}")
        print(f"Binary Search Time: {binary_time}")
        print()
        

if __name__ == "__main__":
    test_performance()