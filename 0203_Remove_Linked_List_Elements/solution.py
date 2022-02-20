from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        nodes = ListNode(0, head)
        current_nodes = nodes
        while current_nodes.next:
            if current_nodes.next.val == val:
                current_nodes.next = current_nodes.next.next
            else:
                current_nodes = current_nodes.next
        return nodes.next
