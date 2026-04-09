class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return 0

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) + 1

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print("Height Of Tree:", tree_height(root))
