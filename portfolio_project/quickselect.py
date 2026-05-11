import random


class QuickSelect:

    @staticmethod
    def quickselect(arr, k):
        if len(arr) == 1:
            return arr[0]

        pivot = random.choice(arr)

        lows = [x for x in arr if x < pivot]
        highs = [x for x in arr if x > pivot]
        pivots = [x for x in arr if x == pivot]

        if k < len(lows):
            return QuickSelect.quickselect(lows, k)

        elif k < len(lows) + len(pivots):
            return pivots[0]

        else:
            return QuickSelect.quickselect(
                highs,
                k - len(lows) - len(pivots)
            )


if __name__ == "__main__":
    numbers = [7, 10, 4, 3, 20, 15]
    k = 2

    result = QuickSelect.quickselect(numbers, k)

    print(f"{k + 1}rd smallest element is: {result}")