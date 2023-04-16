class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        
        # convert=[0]*len(nums)
        
        # convert[0]=nums[0]*2
        
        prefix=[0]*len(nums)
        
        # prefix[0]=convert[0]
        
        # for i in range(1,len(nums)):
            
            # convert[i]=nums[i]+max(nums[:i+1])
            
        # print(convert)
        
        curr_max=0
        
        for i in range(0,len(nums)):
            
            curr_max=max(curr_max,nums[i])
            
            prefix[i]=prefix[i-1]+curr_max+nums[i]
            
                # prefix[i]=prefix[i-1]+(nums[i]+max(nums[:i+1]))
                
        return prefix