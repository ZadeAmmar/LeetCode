class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_num = 0
        
        for i in range(len(s) - 1, -1, -1):
            curr_num = roman[s[i]]
            if curr_num < prev_num:
                result -= curr_num
            else:
                result += curr_num
            prev_num = curr_num
        
        return result
        