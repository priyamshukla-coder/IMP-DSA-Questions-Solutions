# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q1=deque([])
        
        res=[]
        
        q1.append(root)
        
        while len(q1)>0:
            
#             node=q1.popleft()
            
#             curr.append(node)
            
            n=len(q1)
            
            curr=[]
            
            for i in range(n):
                
                node=q1.popleft()
            
                curr.append(node.val)
                
                if node.left is not None:
                    
                    q1.append(node.left)
                    
                if node.right is not None:
                    
                    q1.append(node.right)
                    
            res.append(float(sum(curr)/len(curr)))
            
        return res
                       
            
                    
                
                    
            
            
            