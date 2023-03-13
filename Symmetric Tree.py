# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(root1,root2):

            if root1 is None and root2 is None:

                return True

            if root1 is not None and root2 is not None:

                if root1.val == root2.val:

                    a1,a2=symmetric(root1.left,root2.right),symmetric(root2.left,root1.right)

                    return a1 and a2

            return False

        if root is None:

            return True

        return symmetric(root.left,root.right)