class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        seen=[i for i in range(1,len(nums)+1)]
        
        res=[]
        
        c=Counter(nums)
        
        for i in seen:
            
            if c[i]>1:
                
                res.append(i)
                
        for i in seen:
            
            if i not in c:
                
                res.append(i)
                
        return res
                
                