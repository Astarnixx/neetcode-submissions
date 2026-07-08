# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # For each node in preorder: 1. Create a node 2. Find index in inorder using hashmp
        #3. Recursively build left and right subtree by splitting the range l,r.
        #Make hash map of inorder
        indices = {val: idx for idx,val in enumerate(inorder)}
        self.pre_idx = 0 #Global var tracking idx in preorder
        def dfs(l,r):
            if l>r:
                return None
            root_val = preorder[self.pre_idx] #Creating node for preorder value
            self.pre_idx += 1 #Increment preorder index for the next recursion
            root = TreeNode(root_val)
            mid = indices[root_val] #index corresponding to that value in inorder
            #Now we recursively search the left and right side
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(inorder)-1)