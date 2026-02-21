# BLOCK 1: Node class
# SUMMARY:
# - One "box" in the queue.
# - It stores:
#     data -> value
#     next -> link to the next node
# ------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data      # store value
        self.next = None      # link to next node


# ------------------------------------------------------------
# BLOCK 2: Queue class (Linked List implementation)
# SUMMARY:
# - Queue follows FIFO (First In First Out)
# - front points to the first element (remove happens here)
# - rear points to the last element  (insert happens here)
# ------------------------------------------------------------
class Queue:
    def __init__(self):
        self.front = None     # first node
        self.rear = None      # last node


    # --------------------------------------------------------
    # BLOCK 3: Enqueue (insert)
    # SUMMARY:
    # - Adds a new value at the REAR (end).
    # Cases:
    #   1) If queue is empty (rear is None):
    #       front = rear = new_node
    #   2) Else:
    #       rear.next = new_node
    #       rear = new_node
    # Time: O(1)
    # --------------------------------------------------------
    def enqueue(self, data):
        new_node = Node(data)              # create node

        # Case 1: empty queue
        if self.rear is None:
            self.front = self.rear = new_node
            return

        # Case 2: non-empty queue
        self.rear.next = new_node          # link old rear to new node
        self.rear = new_node               # move rear to new node


    # --------------------------------------------------------
    # BLOCK 4: Dequeue (remove)
    # SUMMARY:
    # - Removes one value from the FRONT.
    # Cases:
    #   1) If queue empty -> print message
    #   2) Else:
    #       temp = front
    #       front = front.next
    #       if front becomes None => queue became empty, so rear = None
    # Time: O(1)
    # --------------------------------------------------------
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        temp = self.front                   # node to remove
        self.front = temp.next              # move front forward

        # if queue becomes empty after dequeue
        if self.front is None:
            self.rear = None

        return temp.data                    # return removed value


    # --------------------------------------------------------
    # BLOCK 5: Peek (see front)
    # SUMMARY:
    # - Returns the FRONT value without removing it.
    # Time: O(1)
    # --------------------------------------------------------
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data


    # --------------------------------------------------------
    # BLOCK 6: Display queue
    # SUMMARY:
    # - Prints queue values from FRONT to REAR like:
    #   10 -> 20 -> 30 -> None
    # Time: O(n)
    # --------------------------------------------------------
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    # --------------------------------------------------------
    # BLOCK 7: Search
    # SUMMARY:
    # - Checks whether a value exists in the queue.
    # - Returns True if found, False otherwise.
    # Time: O(n)
    # --------------------------------------------------------
    def search(self, key):
        temp = self.front
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False


# ------------------------------------------------------------
# BLOCK 8: Usage / Example run
# SUMMARY:
# - Enqueue values: 10, 20, 30
# - Display queue
# - Peek front
# - Dequeue one value
# - Display again
# - Search values
# ------------------------------------------------------------
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    q.display()
    # Output: 10 -> 20 -> 30 -> None

    print("Peek:", q.peek())   # 10

    q.dequeue()

    q.display()
    # Output: 20 -> 30 -> None

    print(q.search(30))   # True
    print(q.search(100))  # False
