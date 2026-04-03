class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    max_sum = float("-inf")

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        # Ignore negative paths
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Best path passing through current node
        current_path_sum = node.val + left_gain + right_gain

        # Update global answer
        max_sum = max(max_sum, current_path_sum)

        # Return best one-side path to parent
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


# Example usage
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(max_path_sum(root))
