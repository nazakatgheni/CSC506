import time
import random
from bst import BST
from map_bst import BSTMap

# CREATE BST + MAP
bst = BST()
bst_map = BSTMap()

# GENERATE 50 DATA ITEMS
data = [(random.randint(1, 1000), f"value_{i}") for i in range(50)]

# INSERT DATA
for key, value in data:
    bst.insert(key, value)
    bst_map.put(key, value)

print("\n--- TREE STRUCTURE ---")
bst.print_tree(bst.root)

# TRAVERSALS
print("\n--- INORDER ---")
print(bst.inorder())

print("\n--- PREORDER ---")
print(bst.preorder())

print("\n--- POSTORDER ---")
print(bst.postorder())

# SEARCH TEST
search_key = data[10][0]
print(f"\nSearch {search_key}:", bst.search(search_key))

# MIN/MAX
print("\nMin:", bst.find_min())
print("Max:", bst.find_max())

# BALANCE CHECK
print("\nIs Balanced:", bst.is_balanced())

# DELETE TEST
delete_key = data[5][0]
print(f"\nDeleting {delete_key}...")
bst.delete(delete_key)

print("\n--- TREE AFTER DELETE ---")
bst.print_tree(bst.root)

# PERFORMANCE COMPARISON
search_key = data[20][0]

# BST SEARCH
start = time.time()
bst.search(search_key)
bst_time = time.time() - start

# LIST SEARCH
start = time.time()
for k, v in data:
    if k == search_key:
        break
list_time = time.time() - start

print("\n--- PERFORMANCE ---")
print("BST Search Time:", bst_time)
print("List Search Time:", list_time)