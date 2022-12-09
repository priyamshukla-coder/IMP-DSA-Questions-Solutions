# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(mx,mn,root):

            if root is None:

                return mx-mn

            mx,mn=max(mx,root.val),min(mn,root.val)

            return max(dfs(mx,mn,root.left),dfs(mx,mn,root.right))

        return dfs(float("-inf"),float("inf"),root)

            

            