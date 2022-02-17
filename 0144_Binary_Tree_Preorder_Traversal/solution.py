from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root: TreeNode, passed_nodes: List[int]) -> List[int]:
            tmp = passed_nodes + [root.val]
            if root.left is not None:
                tmp = preorder(root.left, tmp)
            if root.right is not None:
                tmp = preorder(root.right, tmp)
            return tmp

        if root is None:
            return []
        else:
            return preorder(root, [])
