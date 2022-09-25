# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def traverse(root,res,s):
            
            if root == None:
                
                return 
            
            s=s+str(root.val)
            
            if root.left == None and root.right == None:
                
                res.append(s)
                
            s=s+"->"
            
            traverse(root.left,res,s)
            traverse(root.right,res,s)
            
        s=""
        
        res=[]
        
        traverse(root,res,s)
        
        return res