class GraphAdjMatrix:
    def __init__(self):
        self.vertices = []
        self.matrix = []

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)

            # expand existing rows
            for row in self.matrix:
                row.append(0)

            # add new row
            self.matrix.append([0] * len(self.vertices))

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        i = self.vertices.index(u)
        j = self.vertices.index(v)

        self.matrix[i][j] = 1
        self.matrix[j][i] = 1  # undirected

    def remove_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            i = self.vertices.index(u)
            j = self.vertices.index(v)

            self.matrix[i][j] = 0
            self.matrix[j][i] = 0

    def remove_vertex(self, v):
        if v in self.vertices:
            index = self.vertices.index(v)

            self.vertices.pop(index)
            self.matrix.pop(index)

            for row in self.matrix:
                row.pop(index)

    def get_neighbors(self, v):
        neighbors = []
        if v in self.vertices:
            index = self.vertices.index(v)
            for i, val in enumerate(self.matrix[index]):
                if val == 1:
                    neighbors.append(self.vertices[i])
        return neighbors

    def display(self):
        print("\nAdjacency Matrix Representation:")
        print("Vertices:", self.vertices)
        for row in self.matrix:
            print(row)