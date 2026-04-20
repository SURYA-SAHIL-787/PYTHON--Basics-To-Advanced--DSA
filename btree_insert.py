class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    def split_child(self, parent, i):
        t = self.t
        node = parent.children[i]
        new_node = BTreeNode(node.leaf)
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, node.keys[t - 1])

        new_node.keys = node.keys[t:(2 * t) - 1]
        node.keys = node.keys[0:t - 1]

        if not node.leaf:
            new_node.children = node.children[t:2 * t]
            node.children = node.children[0:t]

    def print_tree(self, node, level=0):
        print("Level", level, "Keys:", node.keys)
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

btree = BTree(3)

for key in [10, 20, 5, 6, 12, 30, 7, 17]:
    btree.insert(key)

btree.print_tree(btree.root)
