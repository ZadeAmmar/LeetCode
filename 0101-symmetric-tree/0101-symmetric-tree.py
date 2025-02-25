# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        # recursively compare left and right child?
        if root == None:
            return True
        return self.recurse(root.left, root.right)
    
    def recurse(self, left, right):
        # checks the left and right subtrees to ensure they are symmetrical.
        if left == None and right == None:
            return True
        if left != None and right == None or left == None and right != None:
            return False
        if left.val == right.val:
            return self.recurse(left.left, right.right) and self.recurse(left.right, right.left)
        else:
            return False