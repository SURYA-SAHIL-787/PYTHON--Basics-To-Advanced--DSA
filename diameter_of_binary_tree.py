class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.diameter = 0

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        self.diameter = max(self.diameter, left_height + right_height)

        return 1 + max(left_height, right_height)

    def diameter_of_binary_tree(self, root):
        self.height(root)
        return self.diameter


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    print("Diameter of Binary Tree:", sol.diameter_of_binary_tree(root))
