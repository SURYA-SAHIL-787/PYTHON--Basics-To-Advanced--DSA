# detect_cycle_in_directed_graph.py

from collections import defaultdict


class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs_cycle_check(self, node, visited, recursion_stack):
        visited[node] = True
        recursion_stack[node] = True

        for neighbor in self.graph[node]:
            # If neighbor not visited, explore it
            if not visited[neighbor]:
                if self._dfs_cycle_check(neighbor, visited, recursion_stack):
                    return True

            # If neighbor is in current recursion stack, cycle exists
            elif recursion_stack[neighbor]:
                return True

        # Backtracking: remove node from recursion stack
        recursion_stack[node] = False
        return False

    def has_cycle(self):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices

        for node in range(self.vertices):
            if not visited[node]:
                if self._dfs_cycle_check(node, visited, recursion_stack):
                    return True

        return False


if __name__ == "__main__":
    g = DirectedGraph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)  # creates cycle

    print("Cycle detected:" if g.has_cycle() else "No cycle found")
