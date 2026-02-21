# - A Node is one "box" in the list.
# - It stores:
#     data -> value
#     next -> link to next node
# - In circular list: last node's next points back to head.
# ------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # value stored in this node
        self.next = None      # link to next node (will become circular later)


# ------------------------------------------------------------
# BLOCK 2: CircularLinkedList class (controller)
# SUMMARY:
# - Manages all nodes of circular linked list.
# - head points to the first node.
# - If head is None => list is empty
# - If list has 1 node: node.next points to itself
# ------------------------------------------------------------
class CircularLinkedList:
    def __init__(self):
        self.head = None


    # --------------------------------------------------------
    # BLOCK 3: Insert at beginning
    # SUMMARY:
    # - Adds a new node at the START of the circular list.
    # Cases:
    #   1) Empty list:
    #       new_node.next = new_node (points to itself)
    #       head = new_node
    #   2) Non-empty list:
    #       Find the last node (whose next == head)
    #       last.next = new_node
    #       new_node.next = old head
    #       head = new_node
    # --------------------------------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case 1: empty list
        if self.head is None:
            new_node.next = new_node   # circular: points to itself
            self.head = new_node
            return

        # Case 2: non-empty list -> find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        # connect last node to new node
        temp.next = new_node
        # connect new node to old head
        new_node.next = self.head
        # update head
        self.head = new_node


    # --------------------------------------------------------
    # BLOCK 4: Insert at end
    # SUMMARY:
    # - Adds a new node at the END of the circular list.
    # Cases:
    #   1) Empty list:
    #       new_node.next = new_node
    #       head = new_node
    #   2) Non-empty:
    #       Find last node (next == head)
    #       last.next = new_node
    #       new_node.next = head (to keep circular)
    # --------------------------------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)

        # Case 1: empty list
        if self.head is None:
            new_node.next = new_node   # circular: points to itself
            self.head = new_node
            return

        # Case 2: non-empty -> find last node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        # attach new node at the end
        temp.next = new_node
        new_node.next = self.head      # keep it circular


    # --------------------------------------------------------
    # BLOCK 5: Display list
    # SUMMARY:
    # - Prints nodes starting from head and stops when it reaches head again.
    # - We use while True because there is NO None ending in circular list.
    # - Output ends with "(back to head)" to show the cycle.
    # --------------------------------------------------------
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:      # we came back to start
                break
        print("(back to head)")


    # --------------------------------------------------------
    # BLOCK 6: Delete a node by value (key)
    # SUMMARY:
    # - Deletes the FIRST node whose data == key.
    # Cases:
    #   1) Empty list -> nothing to delete
    #   2) Deleting a normal node (not head):
    #       prev.next = curr.next
    #   3) Deleting head:
    #       Find last node
    #       last.next = head.next
    #       head = head.next
    # - If we complete a full circle and don't find key -> "Value not found"
    # --------------------------------------------------------
    def delete(self, key):
        if self.head is None:
            return

        curr = self.head
        prev = None

        while True:
            # if node to delete is found
            if curr.data == key:
                if prev:
                    # deleting non-head node
                    prev.next = curr.next
                else:
                    # deleting head node
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next

                    # now temp is last node
                    temp.next = curr.next
                    self.head = curr.next

                return  # delete done

            prev = curr
            curr = curr.next

            # if we reached head again, key not found
            if curr == self.head:
                print("Value not found")
                return


    # --------------------------------------------------------
    # BLOCK 7: Search
    # SUMMARY:
    # - Returns True if key exists in the circular list.
    # - Returns False if not found after one full circle.
    # --------------------------------------------------------
    def search(self, key):
        if self.head is None:
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False


# ------------------------------------------------------------
# BLOCK 8: Usage / Example run
# SUMMARY:
# - Creates circular linked list
# - Inserts values
# - Displays list
# - Deletes a value
# - Displays again
# - Searches values
# ------------------------------------------------------------
if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_beginning(5)
    cll.insert_at_end(30)

    cll.display()
    # Output: 5 -> 10 -> 20 -> 30 -> (back to head)

    cll.delete(10)
    cll.display()
    # Output: 5 -> 20 -> 30 -> (back to head)

    print(cll.search(20))    # True
    print(cll.search(100))   # False
