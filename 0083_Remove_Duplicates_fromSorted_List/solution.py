# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li = []
        while head:
            li.append(head.val)
            head = head.next
        s = set(li)
        a = None
        while s:
            m = max(s)
            a = ListNode(m, a)
            s.remove(m)
        return a
