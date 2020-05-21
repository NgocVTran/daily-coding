"""
Implement Binary Search Tree
"""


class Tree():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if (root.left) and (root.right):
            insert(root.left, node)

        if root.left is None:
            root.left = node
            return root

        if root.right is None:
            root.right = node
            return root





# def in_order(root):
#     if root:
#         in_order(root.left)
#         print(root.val)
#         in_order(root.right)


if "__main__" == __name__:
    # r = Tree(50)
    # r.left = Tree(20)
    # r.right = Tree(30)
    #
    # r.left.left = Tree(40)



    r = Tree(50)
    insert(r, Tree(30))
    insert(r, Tree(20))
    insert(r, Tree(40))
    insert(r, Tree(70))
    insert(r, Tree(60))
    insert(r, Tree(80))

    # insert(r, Tree(70))
    # insert(r, Tree(60))
    # insert(r, Tree(80))

    # in_order(r)
    # print("r:", r)
    # print("r:", r.val)
    # print("r:", r.left.val)
    # print("r:", r.right.val)


# Recursive Python program for level order traversal of Binary Tree

# # A node structure
# class Node:
#
#     # A utility function to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
#
# # Function to  print level order traversal of tree
# def printLevelOrder(root):
#     h = height(root)
#     for i in range(1, h + 1):
#         printGivenLevel(root, i)
#
#     # Print nodes at a given level
#
#
# def printGivenLevel(root, level):
#     if root is None:
#         return
#     if level == 1:
#         print
#         "%d" % (root.data),
#     elif level > 1:
#         printGivenLevel(root.left, level - 1)
#         printGivenLevel(root.right, level - 1)
#
#
# """ Compute the height of a tree--the number of nodes
#     along the longest path from the root node down to
#     the farthest leaf node
# """
# def height(node):
#     if node is None:
#         return 0
#     else:
#         # Compute the height of each subtree
#         lheight = height(node.left)
#         rheight = height(node.right)
#
#         # Use the larger one
#         if lheight > rheight:
#             return lheight + 1
#         else:
#             return rheight + 1
#
#
# # Driver program to test above function
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
#
# print
# "Level order traversal of binary tree is -"
# printLevelOrder(root)
#
#

