# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(root,res=[]):
            
            if root==None:
                return 
            
            res.append(str(root.val))
            
            if root.left == None and root.right == None:
                return
            
            if root.left!=None:
                
                res.append("(")
                preorder(root.left,res)
                res.append(")")
                
            if root.right!=None:
                
                if root.left==None:
                    res.append("()")
                
                res.append("(")
                preorder(root.right,res)
                res.append(")")
            
        res=[]
        preorder(root,res)
        return "".join(res)
    