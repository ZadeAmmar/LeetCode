class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # iterate over both arrays with a running pointer to them both. just like merge sort
        lastnum1 = m-1
        lastnum2 = n-1
        if lastnum1 == -1 and lastnum2 != -1:
            for x in range(n):
                nums1[x] = nums2[x]
        last = m+n-1
        while lastnum1 != -1 and lastnum2 != -1:
            if nums1[lastnum1] > nums2[lastnum2]:
                nums1[last] = nums1[lastnum1]
                lastnum1 -= 1
            else:
                nums1[last] = nums2[lastnum2]
                lastnum2 -= 1
            last -= 1
        if lastnum2 != 0:
            for x in range(lastnum2):
                nums1[x] = nums2[x]


        