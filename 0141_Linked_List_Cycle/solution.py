from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        done = 999999
        while head is not None:
            if head.val == done:
                return True
            else:
                head.val = done
                head = head.next
        return False
