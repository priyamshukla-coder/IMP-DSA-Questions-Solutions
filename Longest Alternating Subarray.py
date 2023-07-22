class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        
        cnt=0
        
        for i in range(len(nums)-1):
            
            j=i+1
            
            while j<len(nums) and nums[j]==nums[i]+((j-i)%2):
                
                cnt=max(cnt,j-i+1)
                
                j=j+1
                
        return cnt if cnt>1 else -1
                
        