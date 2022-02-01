from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def _depth_of_tree(root: TreeNode, depth: int) -> int:
            d = depth
            if root.left is None:
                pass
            else:
                d = max(d, _depth_of_tree(root.left, depth + 1))

            if root.right is None:
                pass
            else:
                d = max(d, _depth_of_tree(root.right, depth + 1))
            return d

        return _depth_of_tree(root, 0)
