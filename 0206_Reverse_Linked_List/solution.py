from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _reverse(head: ListNode) -> ListNode:
            nodes = ListNode(head.val)
            while head.next is not None:
                nodes = ListNode(head.next.val, nodes)
                head.next = head.next.next
            return nodes

        if head is None:
            return None
        else:
            return _reverse(head)
