class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def copy_path(path):
    head = None
    tail = None

    for val in path:
        node = ListNode(val)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node

    return head


def get_paths(root, path, result):
    if not root:
        return

    path.append(root.val)

    if not root.left and not root.right:
        result.append(copy_path(path))
    else:
        get_paths(root.left, path, result)
        get_paths(root.right, path, result)

    path.pop()


def print_lists(lists):
    for head in lists:
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

res = []
get_paths(root, [], res)

print_lists(res)
