from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_graph(root, graph):
    if not root:
        return
    
    if root.left:
        graph[root.val].append(root.left.val)
        graph[root.left.val].append(root.val)
        build_graph(root.left, graph)

    if root.right:
        graph[root.val].append(root.right.val)
        graph[root.right.val].append(root.val)
        build_graph(root.right, graph)


def shortest_path(root, start, end):
    graph = defaultdict(list)
    build_graph(root, graph)

    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))

    return -1


# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Shortest Distance:", shortest_path(root, 4, 3))
