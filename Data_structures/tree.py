import numpy as np
import math
import test
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def insert(self, data):
        #compare new node with parent
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

        ##findval METHOD TO COMPARE
        ##VALUE WITH NODES
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data)+' is found')
    def maxDepth(node):
        if node is None:
            return 0;
        else:
            #depth of each subtree.
            lDepth = maxDepth(node.left)
            rDepth = maxDepth(node.right)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

root = Node(10)
root.insert(6)
root.insert(14)
root.PrintTree()
print(root.findval(6))
root.left = Node(2)
root.right = Node(3)
root.left.left = Node (4)

# Python3 program to find the maximum depth of tree

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node
def maxDepth(node):
    if node is None:
        return 0 ;

    else :

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print ("Height of tree is %d" %(maxDepth(root)))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

#    find maximum depth of a tree.
# https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/

#   find if binary tree is height balanced:
# https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/?ref=rp


#An empty tree is height-balanced. A non-empty binary tree T is balanced if:
#1) Left subtree of T is balanced
#2) Right subtree of T is balanced
#3) The difference between heights of left subtree and right subtree is not more than 1.

    def is_balanced(self):
        return abs(
                self.right_node.depth() if self.right_node != None else 0
                -
                self.left_node.depth() if self.left_node != None else 0
        ) <= 1

    def balance(self):
        #1. Get all array values, sorted.
