# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        # recursive solution - recursively swap children 
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        elif root.left != None and root.right != None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
        elif root.left != None:
            self.invertTree(root.left)
            temp = root.left
            root.left = root.right
            root.right = temp
        else:
            self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
        return root
            
        