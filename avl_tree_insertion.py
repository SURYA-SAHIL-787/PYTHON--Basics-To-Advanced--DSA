class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def get_balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = insert(root, value)

preorder(root)
