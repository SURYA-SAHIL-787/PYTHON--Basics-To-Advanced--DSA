import java.util.*;

public class InorderTraversal {

    // Definition for a binary tree node
    static class TreeNode {
        int val;
        TreeNode left, right;

        TreeNode(int val) {
            this.val = val;
        }
    }

    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorder(root, result);
        return result;
    }

    private static void inorder(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }

        inorder(node.left, result);
        result.add(node.val);
        inorder(node.right, result);
    }

    public static void main(String[] args) {
        /*
                1
                 \
                  2
                 /
                3
        */

        TreeNode root = new TreeNode(1);
        root.right = new TreeNode(2);
        root.right.left = new TreeNode(3);

        System.out.println(inorderTraversal(root)); // [1, 3, 2]
    }
}
