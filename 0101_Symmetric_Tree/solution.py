from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _is_same_tree(left: TreeNode, right: TreeNode, f: bool) -> bool:
            if not f:
                return False
            if (left.left is None) and (right.right is None):
                pass
            elif (left.left is None) or (right.right is None):
                return False
            else:
                f = _is_same_tree(left.left, right.right, f)

            if left.val != right.val:
                return False

            if (left.right is None) and (right.left is None):
                pass
            elif (left.right is None) or (right.left is None):
                return False
            else:
                f = _is_same_tree(left.right, right.left, f)
            return f

        if root is None:
            return False
        if (root.left is None) and (root.right is None):
            return True
        elif (root.left is None) or (root.right is None):
            return False
        else:
            return _is_same_tree(root.left, root.right, True)
