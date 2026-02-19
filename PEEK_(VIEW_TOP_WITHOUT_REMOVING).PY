def peek(self):
    if self.top is None:
        print("Stack is empty")
        return None
    return self.top.data
