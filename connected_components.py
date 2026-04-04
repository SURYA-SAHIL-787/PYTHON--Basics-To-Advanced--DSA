# connected_components.py

from collections import defaultdict

def count_components(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            components += 1
            dfs(node)

    return components


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print("Connected Components:", count_components(n, edges))
  
