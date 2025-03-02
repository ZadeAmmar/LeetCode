# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        elif root.left != None and root.right != None:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        elif root.left != None:
            return self.postorderTraversal(root.left) + [root.val]
        else:
            return self.postorderTraversal(root.right) + [root.val]
        
        