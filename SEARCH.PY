def search(self, key):
    temp = self.head
    while temp:
        if temp.data == key:
            return True
        temp = temp.next
    return False
