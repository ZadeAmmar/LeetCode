class Solution(object):
    def containsDuplicate(self, nums):
        extra = set()
        for x in nums:
            if x in extra:
                return True
            extra.add(x)
        return False
        