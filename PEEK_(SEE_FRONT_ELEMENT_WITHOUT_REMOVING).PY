def peek(self):
    if self.front is None:
        print("Queue is empty")
        return None
    return self.front.data
