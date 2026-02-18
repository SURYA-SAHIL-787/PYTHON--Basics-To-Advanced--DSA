def search(self, key):
    temp = self.front
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False
