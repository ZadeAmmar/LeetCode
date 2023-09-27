class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        start = 0
        end = x // 2
        answer = 0

        while start <= end:
            
            mid = (start + end) // 2 

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid + 1
                answer = mid 
            else:
                end = mid - 1

        return answer

        
        
        