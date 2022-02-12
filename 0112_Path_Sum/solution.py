from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def _has_path_sum(root: TreeNode, target: int) -> bool:
            flag = False
            target -= root.val
            if root.left is None and root.right is None:
                return target == 0
            else:
                if root.left is not None:
                    flag = _has_path_sum(root.left, target) or flag
                if root.right is not None:
                    flag = _has_path_sum(root.right, target) or flag
                return flag

        if root is None:
            return False
        else:
            return _has_path_sum(root, targetSum)
