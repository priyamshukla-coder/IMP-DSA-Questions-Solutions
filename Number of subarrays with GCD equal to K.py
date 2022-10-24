class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        cnt=0
        
        for i in range(len(nums)):
            
            val=nums[i]
            
            for j in range(i,len(nums)):
                
                val=gcd(val,nums[j])
                
                if val==k:
                    
                    cnt=cnt+1
                    
        return cnt