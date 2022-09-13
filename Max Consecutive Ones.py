class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        mx=0
        
        cnt=0
        
        for i in nums:
            
            if i==1:
                
                cnt=cnt+1
                
                mx=max(mx,cnt)
                
            else:
                
                cnt=0
                
        return mx