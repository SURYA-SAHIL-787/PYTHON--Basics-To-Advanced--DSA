# dijkstra_shortest_path.py

import heapq


def dijkstra(graph, start):
    """
    graph format:
    {
        'A': [('B', 4), ('C', 1)],
        'B': [('D', 1)],
        'C': [('B', 2), ('D', 5)],
        'D': []
    }
    """

    # Step 1: Initialize all distances as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min heap stores (current_distance, node)
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Skip outdated heap entries
        if current_distance > distances[current_node]:
            continue

        # Relax all neighboring edges
        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(min_heap, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 1)],
        'B': [('D', 1)],
        'C': [('B', 2), ('D', 5)],
        'D': []
    }

    source = 'A'
    print("Shortest distances from", source, ":", dijkstra(graph, source))
