class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        
        for i in range(len(nums)):
            
            if nums[i]!=0:
                
                # idx=idx+1
                
                nums[idx]=nums[i]
                
                idx=idx+1
        # print(nums)
                
        for i in range(idx,len(nums)):
            
            nums[i]=0