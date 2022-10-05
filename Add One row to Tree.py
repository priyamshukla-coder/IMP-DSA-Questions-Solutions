# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val =     val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def bfs(root,val,d):
            
            if d==1:
                
                return TreeNode(val,root,None)
            
            q=deque([])
            
            q.append(root)
            d=d-1
            
            while d>0:
                
                n=len(q)
                d=d-1
                
                for _ in range(n):
                    
                    node=q.popleft()
                    
                    nl=node.left
                    
                    nr=node.right
                    
                    if d==0:
                        
                        node.left=TreeNode(val,nl,None)
                        
                        node.right=TreeNode(val,None,nr)
                        
                    if nl:
                        
                        q.append(nl)
                        
                    if nr:
                        
                        q.append(nr)
            
            return root
        
        return bfs(root,val,depth)