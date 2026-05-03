class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(node, visited, rec_stack):
    if not node:
        return False

    if node in rec_stack:
        return True

    if node in visited:
        return False

    visited.add(node)
    rec_stack.add(node)

    if detect_cycle(node.next, visited, rec_stack):
        return True

    rec_stack.remove(node)
    return False


def has_cycle(head):
    return detect_cycle(head, set(), set())


# Example
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c
c.next = a  # cycle

print("Cycle Exists:", has_cycle(a))
