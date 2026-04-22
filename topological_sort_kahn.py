# topological_sort_kahn.py

from collections import deque


def topological_sort(vertices, edges):
    # Build adjacency list and indegree array
    graph = [[] for _ in range(vertices)]
    indegree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    # Push all nodes with indegree 0 into queue
    queue = deque()
    for node in range(vertices):
        if indegree[node] == 0:
            queue.append(node)

    topo_order = []

    while queue:
        current = queue.popleft()
        topo_order.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # If all nodes are not processed, graph has cycle
    if len(topo_order) != vertices:
        return "Topological sort not possible (graph has cycle)"

    return topo_order


if __name__ == "__main__":
    vertices = 6
    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    print("Topological Order:", topological_sort(vertices, edges))
