def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    components = 0
    for node in range(n):
        if node not in visited:
            dfs(node, graph, visited)
            components += 1
    return components
# Example
n = 7
edges = [(0, 1), (1, 2), (3, 4), (5, 6)]
print("Connected Components:", count_components(n, edges))
