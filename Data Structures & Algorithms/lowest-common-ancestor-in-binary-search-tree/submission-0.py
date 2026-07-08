# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if (root.val>p.val and root.val<q.val) or (root.val<p.val and root.val>q.val) or (root.val==p.val) or (root.val==q.val):
            return root #If p and q are on different subtrees / node is p or q
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)