# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,low=float('-inf'),high=float('inf')):
            if not node:
                return True
            if not (low<node.val<high): # The current node's value must fit within the current boundaries
                return False
            # Update boundaries for subtrees:
            # Left child must be less than node.val
            # Right child must be greater than node.val
            return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
        return dfs(root)
            