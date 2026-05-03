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


def lca(root, n1, n2):
    if not root:
        return None

    if n1 < root.key and n2 < root.key:
        return lca(root.left, n1, n2)

    if n1 > root.key and n2 > root.key:
        return lca(root.right, n1, n2)

    return root.key


root = None
values = [40, 20, 60, 10, 30, 50, 70, 25, 35]

for v in values:
    root = insert(root, v)

print("LCA:", lca(root, 25, 35))
