# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root,l1):
            if root is None:
                return

            if root.left==None and root.right==None:
                l1.append(root.val)

            dfs(root.left,l1)
            dfs(root.right,l1)

            return l1

        return dfs(root1,[])==dfs(root2,[])