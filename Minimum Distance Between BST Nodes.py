# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def traverse(root):

            nonlocal prev

            if root is None:

                return float("inf")

            mn=traverse(root.left)

            # if prev:

            #     # print(root.val,prev)

            #     # print(mn)

            mn=min(mn,root.val-prev)

            prev=root.val

            mn=min(mn,traverse(root.right))

            return mn

        prev=float("-inf")

        return traverse(root)