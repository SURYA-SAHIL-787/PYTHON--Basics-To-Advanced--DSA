# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if tree is empty
        if not root:
            return 0
        
        # Recursively find depth of left and right subtree
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return max depth + 1 (current node)
        return 1 + max(left_depth, right_depth)
