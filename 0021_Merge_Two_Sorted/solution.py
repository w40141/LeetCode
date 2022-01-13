# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while not (list1 is None and list2 is None):
            if list1 is None:
                val = list2.val
                list2 = list2.next
            elif list2 is None:
                val = list1.val
                list1 = list1.next
            elif list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            ans.append(val)
        ans = ans[::-1]
        node = None
        for a in ans:
            node = ListNode(a, node)
        return node
