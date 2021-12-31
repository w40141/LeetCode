# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_val = 0
        return self.depth_first_search(root, max_val)
        
    def depth_first_search(self, root_node, max_val):
        # print(root_node)
        max_val = self.calc_depth_first_search(root_node, root_node.val, max_val)
        if root_node.left is not None:
            max_val = self.depth_first_search(root_node.left, max_val)
        if root_node.right is not None:
            max_val = self.depth_first_search(root_node.right, max_val)
        return max_val
        
        
        
    def calc_depth_first_search(self, root_node, val, max_val):
        max_val = max(abs(root_node.val - val), max_val)
        # print(root_node.val, val, max_val)
        if root_node.left is not None:
            max_val = self.calc_depth_first_search(root_node.left, val, max_val)
        if root_node.right is not None:
            max_val = self.calc_depth_first_search(root_node.right, val, max_val)
        return max_val
    
    # def calc_depth_first_search(self, root_node, val, max_val):
    #     if root_node.left is not None:
    #         return self.calc_depth_first_search(root_node.left, val, max_val)
    #     else:
    #         max_val_left = abs(val - root_node.val)
    #     if root_node.right is not None:
    #         return self.calc_depth_first_search(root_node.right, val, max_val)
    #     else:
    #         max_val_right = abs(val - root_node.val)
    #     return max(max_val_left, max_val_right)
