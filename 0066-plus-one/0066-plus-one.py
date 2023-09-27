class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        string = ""

        for x in digits:
            string += str(x)

        arr = list(str(int(string)+1))
        for x in range(len(arr)):
            arr[x] = int(arr[x])

        return arr