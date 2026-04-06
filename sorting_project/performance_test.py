import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insert_sort import insertion_sort
from merge_sort import merge_sort

def measure_time(sort_function, data):
    start = time.time()
    sort_function(data.copy())
    end = time.time()
    return end - start