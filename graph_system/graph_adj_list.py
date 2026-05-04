class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)  # undirected graph

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def remove_vertex(self, v):
        if v in self.graph:
            for neighbor in self.graph[v]:
                self.graph[neighbor].remove(v)
            del self.graph[v]

    def get_neighbors(self, v):
        return self.graph.get(v, [])

    def display(self):
        print("\nAdjacency List Representation:")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")