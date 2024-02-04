class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

        for i in range(1, vertices + 1):
            self.adj_list[i] = []

    def add_edge(self, start, end, weight):
        self.adj_list[start].append([end, weight])

    def ad_list(self):
        print("Adjacency List:")
        for vertex in self.adj_list:
            print(f'"{vertex}": {self.adj_list[vertex]}')

    def ad_mat(self):
        print("\nAdjacency Matrix:")
        matrix = [[0] * self.vertices for _ in range(self.vertices)]

        for vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                end, weight = neighbor
                matrix[int(vertex) - 1][int(end) - 1] = weight  

        for row in matrix:
            print(row)

if __name__ == "__main__":
    g = Graph(4)

    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 4)
    g.add_edge(4, 1, 5)

    g.ad_list()
    g.ad_mat()
