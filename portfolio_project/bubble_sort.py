class BubbleSort:

    @staticmethod
    def sort(numbers):
        arr = numbers[:]
        n = len(arr)
        steps = []

        for i in range(n):
            for j in range(0, n - i - 1):
                steps.append(f"Comparing {arr[j]} and {arr[j + 1]}")

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    steps.append(f"Swapped -> {arr}")

            steps.append(f"End of Pass {i + 1}: {arr}")

        return arr, steps


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data, sorting_steps = BubbleSort.sort(data)

    print("Sorted:", sorted_data)
    print()

    for step in sorting_steps:
        print(step)