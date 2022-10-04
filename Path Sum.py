# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(root,s):
            
            if root is None:
                
                return False
            
            if root.val == s and root.left == None and root.right == None:
                
                return True
            
            return traverse(root.left,s-root.val) or traverse(root.right,s-root.val)
        
        return traverse(root,targetSum)
            
            