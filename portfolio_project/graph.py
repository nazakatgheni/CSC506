class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        return self.graph


if __name__ == "__main__":
    delivery_network = Graph()

    delivery_network.add_vertex("Warehouse")
    delivery_network.add_vertex("Store")
    delivery_network.add_vertex("Customer")

    delivery_network.add_edge("Warehouse", "Store")
    delivery_network.add_edge("Store", "Customer")

    print(delivery_network.display())