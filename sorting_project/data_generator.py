import random

def random_data(size):
    return [random.randint(1, 100000) for _ in range(size)]

def sorted_data(size):
    return list(range(size))

def reverse_sorted_data(size):
    return list(range(size, 0, -1))

def partially_sorted_data(size):
    arr = list(range(size))
    for _ in range(size // 10):
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr