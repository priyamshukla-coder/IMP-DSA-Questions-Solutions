class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        i,j=0,0
        
        res=0
        
        while i<len(colors):
            
            j=i+1
            
            curr=neededTime[i]
            mx=neededTime[i]
            
            while j<len(neededTime) and colors[i]==colors[j]:
                
                curr=curr+neededTime[j]
                
                mx=max(mx,neededTime[j])
                
                j=j+1
                
            res=res+(curr-mx)
            
            i=i+1
            
        return res
                
            
            