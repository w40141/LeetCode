from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def _paths(root: TreeNode, s: str) -> List[str]:
            ans = []
            s += str(root.val) + "->"
            if root.left is None and root.right is None:
                return [s]
            else:
                if root.left is not None:
                    ans += _paths(root.left, s)
                if root.right is not None:
                    ans += _paths(root.right, s)

            return ans

        if root is None:
            return []
        else:
            return [s[:-2] for s in _paths(root, "")]
