# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        elif root.left != None and root.right != None:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        elif root.left != None:
            return [root.val] + self.preorderTraversal(root.left)
        elif root.right != None:
            return [root.val] + self.preorderTraversal(root.right)
        