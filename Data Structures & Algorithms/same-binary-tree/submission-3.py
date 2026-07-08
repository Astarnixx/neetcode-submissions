# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Check if both null or same value - if not, return False
        #If yes, recursively check left and right subtrees.
        queue = [(p,q)]
        while queue:
            node1,node2 = queue.pop(0)
            if (node1==None and node2==None):
                continue
            if not node1 or not node2 or (node1.val!=node2.val):
                return False
            queue.append((node1.left,node2.left))
            queue.append((node1.right,node2.right))
        return True