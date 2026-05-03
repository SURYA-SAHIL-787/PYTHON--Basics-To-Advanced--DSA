class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


def height(root):
    return root.height if root else 0


def balance(root):
    return height(root.left) - height(root.right) if root else 0


def right_rotate(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and key < root.left.key:
        return right_rotate(root)

    if b < -1 and key > root.right.key:
        return left_rotate(root)

    if b > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return right_rotate(root)

    if b > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and balance(root.right) <= 0:
        return left_rotate(root)

    if b < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


root = None
values = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for v in values:
    root = insert(root, v)

root = delete(root, 10)

print("AVL after deletion:")
inorder(root)
