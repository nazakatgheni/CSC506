import csv
from data_generator import *
from performance_test import measure_time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insert_sort import insertion_sort
from merge_sort import merge_sort

sizes = [1000, 5000, 10000, 50000]

datasets = {
    "Random": random_data,
    "Sorted": sorted_data,
    "Reverse": reverse_sorted_data,
    "Partial": partially_sorted_data
}

algorithms = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Merge": merge_sort
}

with open("results.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Algorithm", "DataType", "Size", "Time"])

    for size in sizes:
        for data_type, generator in datasets.items():
            data = generator(size)
            for name, algo in algorithms.items():
                time_taken = measure_time(algo, data)
                writer.writerow([name, data_type, size, time_taken])
                print(name, data_type, size, time_taken)