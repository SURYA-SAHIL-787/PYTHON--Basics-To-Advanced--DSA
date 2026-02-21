# -----------------------------------------------------------
# BLOCK 1: Node class
# SUMMARY:
# - A Node is one single "box" in the linked list.
# - It stores:
#     data -> the value
#     next -> link to the next node (None means no next node)
# ------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # store the value in this node
        self.next = None      # link to next node (empty at first)


# ------------------------------------------------------------
# BLOCK 2: LinkedList class (controller)
# SUMMARY:
# - LinkedList manages all nodes.
# - head points to the first node.
# - If head is None => list is empty
# ------------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None      # start with empty list


    # --------------------------------------------------------
    # BLOCK 3: Insert at beginning
    # SUMMARY:
    # - Adds a new node at the START of the list.
    # Steps:
    #   1) Create new node
    #   2) Point new node's next to current head
    #   3) Update head to new node
    # --------------------------------------------------------
    def insert_at_beginning(self, data):
        new_node = Node(data)        # create node
        new_node.next = self.head    # link new node to old head
        self.head = new_node         # new node becomes head


    # --------------------------------------------------------
    # BLOCK 4: Insert at end
    # SUMMARY:
    # - Adds a new node at the END of the list.
    # Cases:
    #   1) If list empty -> new node becomes head
    #   2) Else -> move to last node and attach new node
    # --------------------------------------------------------
    def insert_at_end(self, data):
        new_node = Node(data)        # create node

        if self.head is None:        # if list is empty
            self.head = new_node     # new node becomes head
            return

        temp = self.head             # start from head
        while temp.next:             # move until last node
            temp = temp.next

        temp.next = new_node         # connect last node to new node


    # --------------------------------------------------------
    # BLOCK 5: Display
    # SUMMARY:
    # - Prints all nodes from head to end like:
    #   5 -> 10 -> 20 -> None
    # - Traverses using temp = temp.next
    # --------------------------------------------------------
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    # --------------------------------------------------------
    # BLOCK 6: Delete by value (key)
    # SUMMARY:
    # - Deletes the FIRST node that matches the key.
    # Cases:
    #   1) If head has key -> move head to next
    #   2) Else find key node and reconnect links to skip it
    #   3) If not found -> print "Value not found"
    # --------------------------------------------------------
    def delete(self, key):
        temp = self.head

        # Case 1: Head node is the one to delete
        if temp and temp.data == key:
            self.head = temp.next
            return

        # Case 2: Search for node to delete
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Case 3: Not found
        if temp is None:
            print("Value not found")
            return

        # Key found: skip the node
        prev.next = temp.next


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
# - Creates a linked list
# - Inserts values (beginning/end)
# - Displays list
# - Deletes a value
# - Displays list again
# - Searches values
# ------------------------------------------------------------
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_beginning(5)
    ll.insert_at_end(30)

    ll.display()          # Output: 5 -> 10 -> 20 -> 30 -> None

    ll.delete(10)
    ll.display()          # Output: 5 -> 20 -> 30 -> None

    print(ll.search(20))   # True
    print(ll.search(100))  # False
