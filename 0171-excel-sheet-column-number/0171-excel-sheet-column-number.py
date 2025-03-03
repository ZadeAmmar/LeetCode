class Solution(object):
    def titleToNumber(self, columnTitle):
        cols = 0
        for x in range(len(columnTitle)):
            cols += (26 ** (len(columnTitle) - x - 1)) * (ord(columnTitle[x])-64)
        return cols
        