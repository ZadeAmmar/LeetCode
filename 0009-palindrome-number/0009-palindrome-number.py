class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = ""
        for z in range(len(x)-1, -1, -1):
            y += x[z]

        if(x == y):
            return True
        return False
        