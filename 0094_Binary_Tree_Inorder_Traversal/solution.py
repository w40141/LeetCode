from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(root, li):
            if root.left is not None:
                traversal(root.left, li)
            li.append(root.val)
            if root.right is not None:
                traversal(root.right, li)

        li: List[int] = []
        if root is not None:
            traversal(root, li)
            return li
        else:
            return li
