import time
import random

from bubble_sort import BubbleSort
from quickselect import QuickSelect


def test_bubble_sort():
    data = [random.randint(1, 10000) for _ in range(500)]

    start = time.time()
    BubbleSort.sort(data)
    end = time.time()

    return end - start


def test_quickselect():
    data = [random.randint(1, 10000) for _ in range(5000)]

    start = time.time()
    QuickSelect.quickselect(data, 50)
    end = time.time()

    return end - start


if __name__ == "__main__":
    bubble_time = test_bubble_sort()
    quickselect_time = test_quickselect()

    print("Bubble Sort Time:", bubble_time)
    print("Quickselect Time:", quickselect_time)