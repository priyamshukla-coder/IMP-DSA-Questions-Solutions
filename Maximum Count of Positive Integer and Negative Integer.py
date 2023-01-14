class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        pos,neg=0,0
        
        for i in nums:
            
            if i<0:
                
                neg=neg+1
                
            elif i>0:
                
                pos=pos+1
                
        return max(pos,neg)