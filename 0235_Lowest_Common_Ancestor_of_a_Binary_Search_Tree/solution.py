class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        min_n = min(p.val, q.val)
        max_n = max(p.val, q.val)
        while True:
            v = root.val
            if v >= min_n and v <= max_n:
                return root
            else:
                if v < min_n:
                    root = root.left
                else:
                    root = root.right
