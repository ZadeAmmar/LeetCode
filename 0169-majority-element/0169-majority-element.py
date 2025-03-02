class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}
        for x in nums:
            if x in hashmap:
                hashmap[x] = hashmap[x] + 1
            else:
                hashmap[x] = 1
        for x in hashmap:
            if hashmap[x] > len(nums)//2:
                return x
        return 0
        