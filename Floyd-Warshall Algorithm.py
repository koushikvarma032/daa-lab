
# Floyd-Warshall Algorithm

INF = float('inf')

# Adjacency matrix of the graph
graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

vertices = len(graph)

# Copy graph into distance matrix
dist = [row[:] for row in graph]

# Floyd-Warshall algorithm
for k in range(vertices):
    for i in range(vertices):
        for j in range(vertices):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

# Display shortest distance matrix
print("Shortest Distance Matrix:")

for i in range(vertices):
    for j in range(vertices):
        if dist[i][j] == INF:
            print("INF", end="\t")
        else:
            print(dist[i][j], end="\t")
    print()
