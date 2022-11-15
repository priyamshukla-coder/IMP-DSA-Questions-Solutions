# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def c(root):
            l,r=root,root
            a,b=0,0
            while l:
                a=a+1
                l=l.left
            while r:
                b=b+1
                r=r.right
            if a==b:
                val=pow(2,a)
                return val-1
            else:
                return 1+c(root.left)+c(root.right)
        if root is None:
            return 0
        return c(root)
        