# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        # exists if there is a path from subchild to leaf such that targetSum = targetSum - root.val
        if root == None:
            return False
        if root.left == None and root.right == None and root.val == targetSum:
            return True
        elif root.left == None and root.right == None and root.val != targetSum:
            return False
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        