# dfs_graph.py

def dfs(graph, node, visited, order):
    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)


# Example
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

visited = set()
order = []
dfs(graph, 0, visited, order)

print("DFS Traversal:", order)
