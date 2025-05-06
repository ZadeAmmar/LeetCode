class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}

        # set the index as the value of the number (key)
        for x in range(len(nums)):
            dictionary[nums[x]] = x


        for x in range(len(nums)):
            if target-nums[x] in dictionary and x != dictionary[target-nums[x]]:
                return [x, dictionary[target-nums[x]]]