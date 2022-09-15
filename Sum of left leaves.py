# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            
            if root is None:
                return 0
            
            
            cur=0
            
            if root.left:
                
                if root.left.left == None and root.left.right == None:
                    
                    cur=cur+root.left.val
                    
                else:
                    
                    cur=cur+traverse(root.left)
                    
            cur=cur+traverse(root.right)
            
            return cur
        
        return traverse(root)
    
    