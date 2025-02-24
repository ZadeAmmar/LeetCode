class Solution(object):
    def climbStairs(self, n):
        array = [1, 1]
        for i in range(2, n+1):
            array.append(array[i-1]+array[i-2])
        return array[n]
        