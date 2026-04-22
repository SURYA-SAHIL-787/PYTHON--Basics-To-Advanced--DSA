# lowest_common_ancestor_bt.py

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    # Base case
    if root is None:
        return None

    # If current node matches one of the targets
    if root.value == p or root.value == q:
        return root

    # Search in left and right subtrees
    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)

    # If both sides returned non-null, current node is LCA
    if left_lca and right_lca:
        return root

    # Otherwise return whichever side found a target
    return left_lca if left_lca else right_lca


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = 7
    q = 4

    lca = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p} and {q} is:", lca.value if lca else None)
