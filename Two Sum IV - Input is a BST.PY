# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s1=set()
        def cal(root,s):
            if root is None:
                return False
            if root.val in s1:
                return True
            s1.add(s-root.val)
            return cal(root.left,s) or cal(root.right,s)
        return cal(root,k)