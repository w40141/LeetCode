from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _invert(root: TreeNode) -> TreeNode:
            left = root.right
            right = root.left
            if left is not None:
                left = _invert(left)
            if right is not None:
                right = _invert(right)
            return TreeNode(root.val, left, right)

        if root:
            return _invert(root)
        else:
            return None
