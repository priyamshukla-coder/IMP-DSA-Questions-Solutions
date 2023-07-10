# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def cal(root):

            if root is None:

                return 0

            if root.left is None:

                return 1+cal(root.right)

            if root.right is None:

                return 1+cal(root.left)

            else:

                return 1+min(cal(root.left),cal(root.right))

        return cal(root)