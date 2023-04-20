#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        
        q1=deque([(root,0)])
        
        mp={}
        
        min_distance_left=0
        
        max_distance_right=0
        
        while len(q1)>0:
            
            node,distance=q1.popleft()
            
            if distance not in mp:
                
                mp[distance]=node.data
                
            if node.left:
                
                q1.append((node.left,distance-1))
                
                min_distance_left=min(min_distance_left,distance-1)
                
            if node.right:
                
                q1.append((node.right,distance+1))
                
                max_distance_right=max(max_distance_right,distance+1)
                
        res=[]
        
        for i in range(min_distance_left,max_distance_right+1):
            
            res.append(mp[i])
            
        return res
