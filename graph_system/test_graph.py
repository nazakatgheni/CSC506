from graph_adj_list import GraphAdjList
from graph_adj_matrix import GraphAdjMatrix
from algorithms import bfs, dfs, shortest_path


def test_adj_list():
    print("\n===== TESTING ADJACENCY LIST =====")

    g = GraphAdjList()

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F")
    ]

    for u, v in edges:
        g.add_edge(u, v)

    g.display()

    bfs(g, "A")
    dfs(g, "A")
    shortest_path(g, "A", "F")


def test_adj_matrix():
    print("\n===== TESTING ADJACENCY MATRIX =====")

    g = GraphAdjMatrix()

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F")
    ]

    for u, v in edges:
        g.add_edge(u, v)

    g.display()

    bfs(g, "A")
    dfs(g, "A")
    shortest_path(g, "A", "F")


if __name__ == "__main__":
    test_adj_list()
    test_adj_matrix()