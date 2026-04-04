# topological_sort.py

from collections import defaultdict

def topo_sort(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in range(n):
        if node not in visited:
            dfs(node)

    return stack[::-1]


if __name__ == "__main__":
    n = 6
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    print("Topological Order:", topo_sort(n, edges))
