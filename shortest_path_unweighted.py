# shortest_path_unweighted.py

from collections import defaultdict, deque

def shortest_path(n, edges, src):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distance = [-1] * n
    distance[src] = 0

    queue = deque([src])

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance


if __name__ == "__main__":
    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [2, 4], [4, 5]]
    src = 0
    print("Shortest distances from source:", shortest_path(n, edges, src))
