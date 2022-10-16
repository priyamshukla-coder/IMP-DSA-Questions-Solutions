class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        d1={}
        
        for i in nums:
            
            if -i in nums:
                
                d1[i]=-i
                
        return max(d1.values()) if len(d1)>0 else -1