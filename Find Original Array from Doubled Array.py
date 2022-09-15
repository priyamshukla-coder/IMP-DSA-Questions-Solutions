class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        if len(changed)%2:
            
            return []
        
        changed.sort()
        
        d1=Counter(changed)
        
        res=[]
        
        for i in changed:
            
            if d1[i]==0:
                
                continue
                
            if d1[i*2]==0:
                
                return []
            
            res.append(i)
            
            d1[i]=d1[i]-1
            
            d1[i*2]=d1[i*2]-1
            
        return res
        
        