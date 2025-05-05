class Solution(object):
    def isAnagram(self, s, t):
        # same number of characters, same characters, same number of each character
        if len(s) != len(t):
            return False
        elif set(s) != set(t):
            return False
        dic_s = {}
        dic_t = {}
        for x in range(len(s)):
            if s[x] in dic_s:
                dic_s[x] += 1
            else:
                dic_s[x] = 1
            if t[x] in dic_t:
                dic_t[x] += 1
            else:
                dic_t[x] = 1
        return dic_s == dic_t
        
        