import random
from linear_search import linear_search
from binary_search import binary_search


def main():
    print("Search Algorithm Tool")
    print("---------------------")

    size = int(input("Enter array size: "))
    arr = random.sample(range(size * 10), size)

    print("\nGenerated Array:")
    print(arr)

    target = int(input("\nEnter number to search: "))

    print("\nChoose search method:")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = input("Enter choice: ")

    if choice == "1":
        index = linear_search(arr, target)
    elif choice == "2":
        arr.sort()
        print("\nSorted Array:")
        print(arr)
        index = binary_search(arr, target)
    else:
        print("Invalid choice")
        return

    if index != -1:
        print("Element found at index:", index)
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
    