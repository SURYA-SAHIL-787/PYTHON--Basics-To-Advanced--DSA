def enqueue(self, data):
    new_node = Node(data)

    if self.rear is None:
        self.front = self.rear = new_node
        return

    self.rear.next = new_node
    self.rear = new_node
