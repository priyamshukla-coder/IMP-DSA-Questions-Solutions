class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        curr=0
        
        # print(len(nums))
        
        if len(nums)%2:
            
            curr=curr+nums[len(nums)//2]
            
        
        st=0
        
        while st<len(nums)//2:
            
            curr=curr+int(str(nums[st])+str(nums[len(nums)-1-st]))
            
            st=st+1
            
        return curr