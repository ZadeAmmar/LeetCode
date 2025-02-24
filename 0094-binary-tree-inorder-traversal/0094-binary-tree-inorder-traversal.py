# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root):
        arr = self.recurse(root)
        arr2 = [0]*len(arr)
        for x in range(len(arr)):
            arr2[x] = arr[x]
        return arr2

    def recurse(self, root):
        arr = []
        # recursively get the left child, then current node, then right child.
        if root == None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        if root.left is not None:
            arr += self.recurse(root.left)
        arr += [root.val]
        if root.right is not None:
            arr += self.recurse(root.right)
        return arr
        