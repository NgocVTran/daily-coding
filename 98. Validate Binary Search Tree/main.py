



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert a new node with the given key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

            # A utility function to do inorder tree traversal


def inorder(root):
    if root:
        inorder(root.left)
        print("inorder", root.val)
        inorder(root.right)

    # Driver program to test the above functions


# Let us create the following BST
#      50
#    /      \
#   30     70
#   / \    / \
#  20 40  60 80
r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
inorder(r)

print("r:", r)
print("r:", r.val)
print("r:", r.left.val)
print("r:", r.right.val)





# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
#     def printer(self):
#         print(self.val)
#
#
# null = -1
# # tree = TreeNode([5, 1, 4, null, null, 3, 6])
# # tree.printer()
# # tree = [5, 1, 4, null, null, 3, 6, null, null, null, null, 7, 8, 7, 4]
# tree = [2, 1, 3]
# print(tree)
#
# def is_valid(tree):
#     for ite in range(len(tree)):
#         if 2*ite+2 < len(tree):
#             # right sub node
#             if tree[2*ite+1] < tree[ite]:
#                 return False
#             # left sub node
#             if tree[2*ite+2] > tree[ite]:
#                 return False
#     return True
# print(is_valid(tree))
#