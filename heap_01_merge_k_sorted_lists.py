import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    tail = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Example
a = ListNode(1, ListNode(4, ListNode(5)))
b = ListNode(1, ListNode(3, ListNode(4)))
c = ListNode(2, ListNode(6))

merged = mergeKLists([a, b, c])
printList(merged)
