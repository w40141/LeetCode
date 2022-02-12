from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root: TreeNode, height: int) -> int:
            if root.left is None and root.right is None:
                return height
            else:
                d = 1000000
                if root.left is not None:
                    d = min(d, depth(root.left, height + 1))
                if root.right is not None:
                    d = min(d, depth(root.right, height + 1))
                return d

        if root is None:
            return 0
        else:
            return depth(root, 1)
