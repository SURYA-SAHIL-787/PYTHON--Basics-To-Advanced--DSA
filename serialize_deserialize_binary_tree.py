class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        values = []

        def preorder(node):
            if node is None:
                values.append("N")
                return

            values.append(str(node.value))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(values)

    def deserialize(self, data):
        values = iter(data.split(","))

        def build_tree():
            value = next(values)

            if value == "N":
                return None

            node = TreeNode(int(value))
            node.left = build_tree()
            node.right = build_tree()
            return node

        return build_tree()


def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value, end=" ")
    inorder_traversal(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    serialized = codec.serialize(root)
    print("Serialized Tree:", serialized)

    deserialized_root = codec.deserialize(serialized)
    print("Inorder Traversal of Deserialized Tree:", end=" ")
    inorder_traversal(deserialized_root)
