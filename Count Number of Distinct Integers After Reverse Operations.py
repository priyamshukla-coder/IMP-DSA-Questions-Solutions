class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        if len(nums)>1 and len(set(nums))==1:
            
            return 1
        
        # res=[]
        
        l=len(nums)
        
        for i in range(l):
        
            
            val=int(str(nums[i])[::-1])
            
            nums.append(val)
            
        return len(set(nums))