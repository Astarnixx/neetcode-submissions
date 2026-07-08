# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Check if both null or same value - if not, return False
        #If yes, recursively check left and right subtrees.
        q1,q2 = deque([p]),deque([q])
        while q1 and q2:
            for i in range(len(q1)):
                node1,node2 = q1.popleft(),q2.popleft()
                if (node1==None and node2==None):
                    continue
                if not node1 or not node2 or (node1.val!=node2.val):
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
        return True