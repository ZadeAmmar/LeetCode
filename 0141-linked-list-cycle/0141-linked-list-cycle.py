# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        elif head.next == None:
            return False
        visited = set()
        cur = head
        while cur.next != None:
            if cur.next in visited:
                return True
            else:
                visited.add(cur.next)
            cur = cur.next
        