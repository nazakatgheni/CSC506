    #
    #  Linear search algorithm
    #  Works on unsorted arrays
    #  Time Complexity: O(n)
    # 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1