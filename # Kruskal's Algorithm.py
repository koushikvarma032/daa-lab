# Kruskal's Algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        result = []

        # Sort edges according to weight
        self.edges.sort(key=lambda edge: edge[2])

        parent = []
        rank = []

        for i in range(self.V):
            parent.append(i)
            rank.append(0)

        edge_count = 0
        i = 0
        total_cost = 0

        while edge_count < self.V - 1:
            u, v, weight = self.edges[i]
            i += 1

            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # Check for cycle
            if root_u != root_v:
                result.append([u, v, weight])
                total_cost += weight
                edge_count += 1
                self.union(parent, rank, root_u, root_v)

        print("Edges in Minimum Spanning Tree:")

        for u, v, weight in result:
            print(u, "--", v, "=", weight)

        print("Total cost:", total_cost)


# Create graph
g = Graph(4)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

# Apply Kruskal's Algorithm
g.kruskal()