class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def flatten(root):
    if not root:
        return None

    left_tail = flatten(root.left)
    right_tail = flatten(root.right)

    if root.left:
        temp = root.right
        root.right = root.left
        root.left = None

        if left_tail:
            left_tail.right = temp

    return right_tail or left_tail or root


def print_list(root):
    while root:
        print(root.val, end=" -> ")
        root = root.right
    print("None")


# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

flatten(root)
print_list(root)
