class Solution(object):
    def containsDuplicate(self, nums):
        numSet = set()
        for x in nums:
            if x in numSet:
                return True
            numSet.add(x)
        return False
        