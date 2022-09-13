from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d1=defaultdict(int)
        
        prefix=[0]*len(nums)
        
        prefix[0]=nums[0]
        
        cnt=0
        
        curr_sum=0
        
#         for i in range(1,len(nums)):
            
#             prefix[i]=prefix[i-1]+nums[i]
            
        for i in nums:
            
            curr_sum=curr_sum+i
            
            if (curr_sum-k) in d1:
                
                cnt=cnt+d1[(curr_sum-k)]
                
            if curr_sum==k:
                
                cnt=cnt+1
                
                
            d1[curr_sum]=d1[curr_sum]+1
            
            # print(d1)
            
        return cnt