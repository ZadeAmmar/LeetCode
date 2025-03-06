class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        extra = {}
        for x in range(len(nums)):
            if nums[x] in extra:
                if abs(extra[nums[x]]-x) <= k:
                    return True
            extra[nums[x]] = x
        return False
        