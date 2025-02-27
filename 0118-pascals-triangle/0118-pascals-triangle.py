class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = [[1]]
        for x in range(1, numRows):
            temp = []
            prev = [0] + triangle[x-1] + [0]
            for y in range(x+1):
                temp.append(prev[y]+prev[y+1])
            triangle.append(temp)
            temp = []
        return triangle

        