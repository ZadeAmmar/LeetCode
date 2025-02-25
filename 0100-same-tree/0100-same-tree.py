# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        boolVar = False
        if p == None or q == None and p!=q:
            return False
        if p.val == q.val:
            boolVar = True
        else:
            return False
        if q.left != None and p.left != None:
            boolVar = boolVar and self.isSameTree(p.left, q.left)
        elif q.left == None and p.left != None or q.left != None and p.left == None:
            return False
        if q.right != None and p.right != None:
            boolVar = boolVar and self.isSameTree(p.right, q.right)
        elif q.right == None and p.right != None or q.right != None and p.right == None:
            return False
        return boolVar
        