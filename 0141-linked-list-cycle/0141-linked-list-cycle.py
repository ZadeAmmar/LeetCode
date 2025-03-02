# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head == None:
            return False
        elif head.next == None:
            return False
        visited = set()
        while head.next != None:
            if head.next in visited:
                return True
            else:
                visited.add(head.next)
            head = head.next