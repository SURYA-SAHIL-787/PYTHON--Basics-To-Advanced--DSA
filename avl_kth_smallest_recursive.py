class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None


def height(root):
    return root.height if root else 0


def size(root):
    return root.size if root else 0


def update(root):
    root.height = 1 + max(height(root.left), height(root.right))
    root.size = 1 + size(root.left) + size(root.right)


def balance(root):
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    update(y)
    update(x)

    return x


def left_rotate(x):
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    update(x)
    update(y)

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

    update(root)
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


def kth_smallest(root, k):
    if not root:
        return None

    left_size = size(root.left)

    if k == left_size + 1:
        return root.key
    elif k <= left_size:
        return kth_smallest(root.left, k)
    else:
        return kth_smallest(root.right, k - left_size - 1)


root = None
values = [100, 50, 150, 25, 75, 125, 175, 60, 90]

for v in values:
    root = insert(root, v)

k = 5
print(f"{k}th Smallest:", kth_smallest(root, k))
