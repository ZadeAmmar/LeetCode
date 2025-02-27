# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.recurse(nums, 0, len(nums)-1)

    def recurse(self, nums, left, right):
        if left > right or nums is None:
            return None
        mid = (left+right)//2
        root = TreeNode(nums[mid])
        root.left = self.recurse(nums, left, mid-1)
        root.right = self.recurse(nums, mid+1, right)
        return root
        
        

