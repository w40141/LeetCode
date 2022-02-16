from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root: TreeNode, passed_nodes: List[int]) -> List[int]:
            if root.left is not None:
                passed_nodes = postorder(root.left, passed_nodes)
            if root.right is not None:
                passed_nodes = postorder(root.right, passed_nodes)
            return passed_nodes + [root.val]

        if root is None:
            return []
        else:
            return postorder(root, [])
