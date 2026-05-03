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


def merge_avl(root1, root2):
    if not root2:
        return root1

    root1 = merge_avl(root1, root2.left)
    root1 = insert(root1, root2.key)
    root1 = merge_avl(root1, root2.right)

    return root1


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


root1 = None
root2 = None

for v in [30, 10, 50, 5, 20]:
    root1 = insert(root1, v)

for v in [40, 15, 60, 35, 70]:
    root2 = insert(root2, v)

merged_root = merge_avl(root1, root2)

print("Merged AVL Tree:")
inorder(merged_root)
