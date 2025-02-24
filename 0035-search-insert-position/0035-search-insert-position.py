class Solution(object):
    def binarySearch(nums, target, left, right, index=0):
        if left > right:
            return -1
        mid = left + (right-left)//2 
        if nums[mid] == target:
            return index
        elif nums[mid] < target:
            return binarySearch(nums, target, mid+1, right, index+mid+1)
        else:
            return binarySearch(nums, target, left, mid-1, index)

    def searchInsert(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1
        elif len(nums) == 1 and nums[0] == target:
            return 0
        if target >= nums[len(nums)-1]:
            return len(nums)
        elif target <= nums[0]:
            return 0
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return mid
    



        