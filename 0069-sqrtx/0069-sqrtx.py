class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        i = 2
        while(True):
            if i * i < x:
                i+=1
                continue

            elif i * i == x:
                return i
                
            else:
                return i-1
        
        
        