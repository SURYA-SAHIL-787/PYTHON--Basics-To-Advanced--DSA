import threading

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.insert(30)
ll.insert(20)
ll.insert(10)

t1 = threading.Thread(target=ll.display)

t1.start()
t1.join()
