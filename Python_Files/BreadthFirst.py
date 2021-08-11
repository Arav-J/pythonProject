class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(branch.root)
        else:
            print("Traversal type" + str(traversal_type) + "is not support")
            return False

    def preorder_print(self, start):
        """Root-> Left -> Right"""
        if start:
            print(start.value)
            self.preorder_print(start.left)
            self.preorder_print(start.right)


# self.preorder_print(start.left)
# self.preorder_print(start.right)
# print(start.value)

#             1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7

# Set up tree:
branch = BinaryTree(1)
branch.root.left = Node(2)
branch.root.right = Node(3)
branch.root.left.left = Node(4)
branch.root.left.right = Node(5)
branch.root.right.left = Node(6)
branch.root.right.right = Node(7)

print(branch.print_tree("preorder"))