# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        links = set()
        while headA is not None:
            links.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in links:
                return headB
            headB = headB.next
        return None
        