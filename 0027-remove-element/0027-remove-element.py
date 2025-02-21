class Solution(object):
    def removeElement(self, nums, val):
        # algorithm: loop through front and back (2 pointers) and swap the first pointer element (if its equal to val) with the second pointer element (if its not equal to val). If first pointer != val, increment, if second pointer = val, decrement
        if nums is None or len(nums) == 0:
            return 0
        tailPtr = len(nums) - 1
        headPtr = 0
        while headPtr < tailPtr:
            while nums[tailPtr] == val and tailPtr > headPtr:
                tailPtr -= 1
            if nums[headPtr] == val:
                temp = nums[tailPtr]
                nums[tailPtr] = nums[headPtr]
                nums[headPtr] = temp
            headPtr += 1

        count = 0
        while count < len(nums) - 1 and nums[count] != val:
            count += 1
        return count

        