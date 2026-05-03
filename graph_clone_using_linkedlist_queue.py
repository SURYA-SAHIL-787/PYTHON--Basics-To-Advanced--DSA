class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        node = QueueNode(val)
        if not self.rear:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if not self.front:
            return None
        val = self.front.val
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def is_empty(self):
        return self.front is None


def clone_graph(node):
    if not node:
        return None

    visited = {}
    queue = LinkedListQueue()

    queue.enqueue(node)
    visited[node] = GraphNode(node.val)

    while not queue.is_empty():
        curr = queue.dequeue()

        for nei in curr.neighbors:
            if nei not in visited:
                visited[nei] = GraphNode(nei.val)
                queue.enqueue(nei)
            visited[curr].neighbors.append(visited[nei])

    return visited[node]


# Example
n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)

n1.neighbors = [n2, n3]
n2.neighbors = [n1, n3]
n3.neighbors = [n1, n2]

clone = clone_graph(n1)
print("Cloned Node:", clone.val)
