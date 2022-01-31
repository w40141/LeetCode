# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _is_same_tree(p: TreeNode, q: TreeNode, f:bool) -> bool:
            if not f:
                return False
            if (p.left is None) and (q.left is None):
                pass
            elif (p.left is None) or (q.left is None):
                return False
            else:
                f = _is_same_tree(p.left, q.left, f)

            if p.val != q.val:
                return False

            if (p.right is None) and (q.right is None):
                pass
            elif (p.right is None) or (q.right is None):
                return False
            else:
                f = _is_same_tree(p.right, q.right, f)
            return f

        if (p is None) and (q is None):
            return True
        elif (p is None) or (q is None):
            return False
        else:
            return _is_same_tree(p, q, True)
