# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #For any given node, longest path through it is sum of height of left and right subtrees
        #Brute: calculate left and right height for each mode using maxDepth function, return max dia found: O(n^2)
        #Optimal - DFS: calculate height while traversing itself
        self.diameter = 0 #Define a variable to keep track of the maximum diameter found so far

        def dfs(node):
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.diameter