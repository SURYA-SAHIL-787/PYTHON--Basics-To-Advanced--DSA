import heapq


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node


def merge_k_lists(lists):
    heap = []
    count = 0

    for node in lists:
        if node:
            heapq.heappush(heap, (node.value, count, node))
            count += 1

    dummy = ListNode(0)
    current = dummy

    while heap:
        value, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.value, count, node.next))
            count += 1

    return dummy.next


def print_list(head):
    while head:
        print(head.value, end=" -> " if head.next else "\n")
        head = head.next


a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

merged = merge_k_lists([a, b, c])
print_list(merged)
