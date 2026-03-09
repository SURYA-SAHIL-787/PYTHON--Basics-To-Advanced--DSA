# Question 10 — Linked List Search
# Write a Python program that:
# 1. Creates a Singly Linked List with n elements.
# 2. Searches for a given value in the linked list.
# 3. Prints the position of the element if found.
# Also print the number of nodes traversed during the search.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self, key):
        temp = self.head
        position = 1
        traversed = 0

        while temp:
            traversed += 1
            if temp.data == key:
                print("Element found at position:", position)
                print("Number of nodes traversed:", traversed)
                return
            temp = temp.next
            position += 1

        print("Element not found")
        print("Number of nodes traversed:", traversed)


sll = SinglyLinkedList()

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    sll.insert_end(value)

key = int(input("Enter value to search: "))
sll.search(key)
