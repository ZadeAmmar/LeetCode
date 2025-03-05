# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev = None
        cur = head
        while cur != None:
            if cur.val == val:
                if prev == None:
                    head = head.next
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head
        