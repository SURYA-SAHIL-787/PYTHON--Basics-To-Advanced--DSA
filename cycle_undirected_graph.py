# cycle_undirected_graph.py

from collections import defaultdict

def has_cycle(n, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in range(n):
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [2, 0], [3, 4]]
    print("Cycle Exists:", has_cycle(n, edges))
