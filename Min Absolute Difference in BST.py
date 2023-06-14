# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def inorder(root,l1):

            if root is None:

                return 

            inorder(root.left,l1)

            l1.append(root.val)

            inorder(root.right,l1)

            return l1

        res=inorder(root,[])

        min_diff=float("inf")

        for i in range(0,len(res)-1):

            min_diff=min(min_diff,abs(res[i+1]-res[i]))

        return min_diff

    