# ------------------------------------------------------------
# BLOCK 1: Node class (Doubly Node)
# SUMMARY:
# - A Node is one "box" in a doubly linked list.
# - It stores:
#     data -> value
#     prev -> link to previous node
#     next -> link to next node
# - Because it has BOTH links, we can move forward and backward.
# ------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # value stored in this node
        self.prev = None      # link to previous node (None initially)
        self.next = None      # link to next node (None initially)


# ------------------------------------------------------------
# BLOCK 2: DoublyLinkedList class (controller)
# SUMMARY:
# - This class manages the whole doubly linked list.
# - head points to the first node.
# - If head is None => list is empty
# ------------------------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # start with empty list


    # --------------------------------------------------------
    # BLOCK 3: Insert at beginning
    # SUMMARY:
    # - Adds a new node at the START.
    # Steps:
    #   1) Create new node
    #   2) If list not empty:
    #        old head's prev -> new node
    #        new node's next -> old head
    #   3) Update head -> new node
    # --------------------------------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)            # create new node

        if self.head is not None:        # if list already has nodes
            self.head.prev = new_node    # old head points back to new node
            new_node.next = self.head    # new node points forward to old head

        self.head = new_node             # new node becomes head


    # --------------------------------------------------------
    # BLOCK 4: Insert at end
    # SUMMARY:
    # - Adds a new node at the END.
    # Cases:
    #   1) If list is empty -> head = new node
    #   2) Else -> go to last node, then connect:
    #        last.next -> new node
    #        new_node.prev -> last
    # --------------------------------------------------------
    # [CREATE ---> CHECK ---> TRAVEL ---> CONNECT:]
    def insert_at_end(self, data):
        new_node = Node(data)            # create new node

        if self.head is None:            # if list is empty
            self.head = new_node         # new node becomes head
            return

        temp = self.head                 # start from head
        while temp.next:                 # move until last node
            temp = temp.next

        temp.next = new_node             # last node points forward to new node
        new_node.prev = temp             # new node points back to last node


    # --------------------------------------------------------
    # BLOCK 5: Display (Forward direction)
    # SUMMARY:
    # - Prints all nodes from head to end like:
    #   5 <-> 10 <-> 20 <-> None
    # - Moves using temp = temp.next
    # --------------------------------------------------------
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


    # --------------------------------------------------------
    # BLOCK 6: Delete by value (key)
    # SUMMARY:
    # - Deletes the FIRST node whose data == key.
    # Steps:
    #   1) Search for the node that has the key
    #   2) If not found -> print "Value not found"
    #   3) If found -> reconnect links on both sides:
    #        left side (prev) should point to right side (next)
    #        right side (next) should point to left side (prev)
    #   Special case:
    #   - If deleting head, head must move to next node
    # --------------------------------------------------------
    def delete(self, key):
        temp = self.head

        # search for key node
        while temp and temp.data != key:
            temp = temp.next

        # if not found
        if temp is None:
            print("Value not found")
            return

        # if temp is not head (has a previous node)
        if temp.prev:
            temp.prev.next = temp.next
        else:
            # temp is head, so move head forward
            self.head = temp.next

        # if temp is not last node (has a next node)
        if temp.next:
            temp.next.prev = temp.prev


    # --------------------------------------------------------
    # BLOCK 7: Search
    # SUMMARY:
    # - Checks if key exists in the list.
    # - Returns True if found, False if not.
    # --------------------------------------------------------
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# ------------------------------------------------------------
# BLOCK 8: Usage / Example run
# SUMMARY:
# - Creates a doubly linked list
# - Inserts values (beginning/end)
# - Displays list
# - Deletes a value
# - Displays again
# - Searches values
# ------------------------------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    dll.insert_at_end(30)

    dll.display()
    # Output: 5 <-> 10 <-> 20 <-> 30 <-> None

    dll.delete(10)
    dll.display()
    # Output: 5 <-> 20 <-> 30 <-> None

    print(dll.search(20))    # True
    print(dll.search(100))   # False
