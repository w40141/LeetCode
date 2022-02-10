from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root: TreeNode, height: int) -> int:
            flag = 1
            if root.left is None:
                flag += 1
                height_left = height
            else:
                height_left = depth(root.left, height + 1)

            if root.right is None:
                flag += 1
                height_right = height
            else:
                height_right = depth(root.right, height + 1)

            if flag == 2:
                return height
            else:
                return min(height_left, height_right)

        if root is None:
            return 0
        else:
            return depth(root, 1)
