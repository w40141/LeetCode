from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root: TreeNode, height: int) -> int:
            height_left = height if root.left is None else check(root.left, height + 1)
            height_right = height if root.right is None else check(root.right, height + 1)

            if height_left == 0 or height_right == 0:
                return 0
            else:
                if abs(height_left - height_right) > 1:
                    return 0
                else:
                    return max(height_left, height_right)

        if root is None:
            return True
        else:
            return True if check(root, 1) else False
