# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def f(root,s1,l1):
            l1.append(root.val)
            if root.left==None and root.right==None:
                if s1==root.val:
                    res.append(l1[:])
            if root.left!=None:
                f(root.left,s1-root.val,l1)
            if root.right!=None:
                f(root.right,s1-root.val,l1)
            l1.pop()
        res=[]
        if root==None:
            return res
        l1=[]
        f(root,targetSum,l1)
        return res
