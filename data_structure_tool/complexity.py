def show_complexity():
    complexity = {
        "Stack": {
            "Push": "O(1)",
            "Pop": "O(1)",
            "Peek": "O(1)"
        },
        "Queue": {
            "Enqueue": "O(1)",
            "Dequeue": "O(1)"
        },
        "Linked List": {
            "Insert": "O(1)",
            "Search": "O(n)",
            "Delete": "O(n)"
        }
    }

    for ds, ops in complexity.items():
        print(ds)
        for op, comp in ops.items():
            print(f"  {op}: {comp}")
        print()