def dequeue(self):
    if self.front is None:
        print("Queue is empty")
        return

    temp = self.front
    self.front = temp.next

    if self.front is None:
        self.rear = None
