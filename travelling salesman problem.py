
def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    visited[start] = True

    def solve(city, count, cost):
        if count == n:
            return cost + graph[city][start]

        ans = float('inf')

        for next_city in range(n):
            if not visited[next_city]:
                visited[next_city] = True

                ans = min(ans, solve(
                    next_city,
                    count + 1,
                    cost + graph[city][next_city]
                ))

                visited[next_city] = False

        return ans

    return solve(start, 1, 0)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print("Minimum travelling cost:", tsp(graph, 0))
