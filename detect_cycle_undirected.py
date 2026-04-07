# detect_cycle_undirected.py

def has_cycle(graph, node, visited, parent):
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, node):
                return True
        elif neighbor != parent:
            return True

    return False


def detect_cycle(n, edges):
    graph = {i: [] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    for node in range(n):
        if node not in visited:
            if has_cycle(graph, node, visited, -1):
                return True

    return False


# Example
n = 5
edges = [(0, 1), (1, 2), (2, 3), (3, 1)]
print("Cycle exists:", detect_cycle(n, edges))
