class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sum = float("-inf")

    def max_gain(self, node):
        if node is None:
            return 0

        left_gain = max(self.max_gain(node.left), 0)
        right_gain = max(self.max_gain(node.right), 0)

        current_path_sum = node.value + left_gain + right_gain
        self.max_sum = max(self.max_sum, current_path_sum)

        return node.value + max(left_gain, right_gain)

    def max_path_sum(self, root):
        self.max_gain(root)
        return self.max_sum


if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print("Maximum Path Sum:", sol.max_path_sum(root))
