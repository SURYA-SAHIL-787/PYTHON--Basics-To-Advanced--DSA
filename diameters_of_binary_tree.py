# diameter_of_binary_tree.py

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeDiameter:
    def __init__(self):
        self.diameter = 0

    def height(self, root):
        if root is None:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        # Update diameter using longest path through current node
        self.diameter = max(self.diameter, left_height + right_height)

        # Return height of subtree
        return 1 + max(left_height, right_height)

    def find_diameter(self, root):
        self.height(root)
        return self.diameter


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    tree = BinaryTreeDiameter()
    print("Diameter of binary tree:", tree.find_diameter(root))
