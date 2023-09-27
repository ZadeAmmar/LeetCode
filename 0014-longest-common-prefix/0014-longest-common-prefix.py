class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for x in range(len(strs[0])):
            curLet = strs[0][x]
            for y in range(1, len(strs)):
                if x >= len(strs[y]) or strs[y][x] != curLet:
                    return prefix
            prefix += curLet

        return prefix
            
        