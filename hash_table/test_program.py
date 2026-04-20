import time
import random
from hash_table import HashTable
from priority_queue import PriorityQueue   

# -----------------------------
# HASH TABLE TEST
# -----------------------------

data = list(range(1000))
random.shuffle(data)

ht = HashTable()

# Insert
for item in data:
    ht.insert(item, item * 10)

# Hash search timing
start = time.time()
for item in data:
    ht.search(item)
ht_search_time = time.time() - start

# Linear search timing
start = time.time()
for item in data:
    for x in data:
        if x == item:
            break
linear_search_time = time.time() - start

print("\n--- Hash Table Performance ---")
print("Hash Search Time:", ht_search_time)
print("Linear Search Time:", linear_search_time)


# -----------------------------
# PRIORITY QUEUE DEMO
# -----------------------------

print("\n--- Priority Queue Demo ---")

pq = PriorityQueue()

pq.insert(5)
pq.insert(2)
pq.insert(8)

print("Peek:", pq.peek())
print("Extract Min:", pq.extract_min())
print("Extract Min:", pq.extract_min())