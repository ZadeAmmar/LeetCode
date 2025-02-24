class Solution(object):
    def lengthOfLastWord(self, s):
        # iterate backwards over the string
        s = s.rstrip(" ")
        if len(s)==1:
            return 1
        length = len(s)
        for i in range(length-1, -1, -1):
            if s[i] == ' ':
                return length - 1 - i
        return len(s)-1
        