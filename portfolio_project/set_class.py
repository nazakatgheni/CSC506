class CustomSet:

    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def contains(self, item):
        return item in self.items

    def union(self, other_set):
        result = CustomSet()

        for item in self.items:
            result.add(item)

        for item in other_set.items:
            result.add(item)

        return result

    def intersection(self, other_set):
        result = CustomSet()

        for item in self.items:
            if item in other_set.items:
                result.add(item)

        return result

    def difference(self, other_set):
        result = CustomSet()

        for item in self.items:
            if item not in other_set.items:
                result.add(item)

        return result

    def symmetric_difference(self, other_set):
        result = CustomSet()

        for item in self.items:
            if item not in other_set.items:
                result.add(item)

        for item in other_set.items:
            if item not in self.items:
                result.add(item)

        return result

    def display(self):
        return self.items


if __name__ == "__main__":
    warehouse_a = CustomSet()
    warehouse_b = CustomSet()

    for item in ["Hammer", "Drill", "Saw"]:
        warehouse_a.add(item)

    for item in ["Saw", "Ladder", "Drill"]:
        warehouse_b.add(item)

    print("Union:", warehouse_a.union(warehouse_b).display())
    print("Intersection:", warehouse_a.intersection(warehouse_b).display())
    print("Difference:", warehouse_a.difference(warehouse_b).display())
    print(
        "Symmetric Difference:",
        warehouse_a.symmetric_difference(warehouse_b).display()
    )