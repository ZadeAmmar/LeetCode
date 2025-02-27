class Solution(object):
    def choose(self, n, k):
        if k > n - k:
            k = n - k
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result

    def getRow(self, rowIndex):
        row = []
        for i in range(rowIndex+1):
            row.append(self.choose(rowIndex, i))
        return row
        