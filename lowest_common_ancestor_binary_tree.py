class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left_lca = lowest_commonAncestor(root.left, p, q)
    right_lca = lowest_commonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


# Correct function name wrapper
def lowest_commonAncestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left_lca = lowest_commonAncestor(root.left, p, q)
    right_lca = lowest_commonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root

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

    p = root.left              # 5
    q = root.left.right.right  # 4

    lca = lowest_commonAncestor(root, p, q)
    print("Lowest Common Ancestor:", lca.value)
