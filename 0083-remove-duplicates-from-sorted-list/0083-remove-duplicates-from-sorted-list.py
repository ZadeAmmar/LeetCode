# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # singly linked list. Each duplicate can only be a dupe of the one before it since its sorted
        if head.next == None:
            return head
        cur = head.next
        prev = head
        while cur is not None:
            if cur.val == prev.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
