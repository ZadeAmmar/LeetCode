class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictionary = {}

        for x in range(len(nums)):
            dictionary[nums[x]] = x


        for x in range(len(nums)):
            if target-nums[x] in dictionary and x != dictionary[target-nums[x]]:
                return [x, dictionary[target-nums[x]]]