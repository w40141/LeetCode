# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return self.addNumbers(l1, l2, 0)

    def addNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], up: int):
        if l1 is None and l2 is None:
            if up > 0:
                return ListNode(up, None)
            else:
                return None
        elif l1 is None:
            x = 0
            next1 = None
            y = l2.val
            next2 = l2.next
        elif l2 is None:
            x = l1.val
            next1 = l1.next
            y = 0
            next2 = None
        else:
            x = l1.val
            y = l2.val
            next1 = l1.next
            next2 = l2.next
        tmp_ans = x + y + up
        return ListNode(tmp_ans % 10, self.addNumbers(next1, next2, tmp_ans // 10))
