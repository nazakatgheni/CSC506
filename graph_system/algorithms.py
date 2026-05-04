from collections import deque


def bfs(graph_obj, start):
    print("\nBFS Traversal (step-by-step):")

    visited = set()
    queue = deque([start])

    while queue:
        print(f"\nQueue: {list(queue)}")

        node = queue.popleft()

        if node not in visited:
            print(f"Visiting: {node}")
            visited.add(node)

            for neighbor in graph_obj.get_neighbors(node):
                if neighbor not in visited:
                    queue.append(neighbor)


def dfs(graph_obj, start):
    print("\nDFS Traversal (step-by-step):")

    visited = set()

    def dfs_recursive(node):
        print(f"Visiting: {node}")
        visited.add(node)

        for neighbor in graph_obj.get_neighbors(node):
            if neighbor not in visited:
                dfs_recursive(neighbor)

    dfs_recursive(start)


def shortest_path(graph_obj, start, end):
    print("\nShortest Path (BFS-based):")

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        print(f"Exploring: {current}, Path so far: {path}")

        if current == end:
            print(f"Shortest path found: {path}")
            return path

        visited.add(current)

        for neighbor in graph_obj.get_neighbors(current):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    print("No path found.")
    return None