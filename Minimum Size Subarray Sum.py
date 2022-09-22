class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        mn=float("inf")
        
        if sum(nums)<target:
            
            return 0
        
        st=0
        
        curr_sum=0
        
        for i in range(len(nums)):
            
            curr_sum=curr_sum+nums[i]
            
#             for j in range(i,len(nums)):
                
#                 curr_sum=curr_sum+nums[j]
                
#                 if curr_sum>=target:
                    
#                     mn=min(mn,j-i+1)
                    
#                     break

            while curr_sum>=target:
        
                mn=min(mn,i+1-st)
            
                curr_sum=curr_sum-nums[st]
                
                st=st+1
                    
        return mn