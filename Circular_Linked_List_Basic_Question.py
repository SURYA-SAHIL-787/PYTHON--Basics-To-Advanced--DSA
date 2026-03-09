Circular Linked List
# Write a Python program that implements a Circular Linked List with the following operations:
# 1. Insert a node
# 2. Delete a node
# 3. Display all elements
# Ensure the last node points back to the first node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete(self, key):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        if current.data == key:
            if current.next == self.head:
                self.head = None
                print("Node deleted")
                return

            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head
            print("Node deleted")
            return

        previous = self.head
        current = self.head.next

        while current != self.head:
            if current.data == key:
                previous.next = current.next
                print("Node deleted")
                return
            previous = current
            current = current.next

        print("Value not found")

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")


cll = CircularLinkedList()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        cll.insert(value)
    elif choice == 2:
        value = int(input("Enter value to delete: "))
        cll.delete(value)
    elif choice == 3:
        cll.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
