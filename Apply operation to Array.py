class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
    
        
        for i in range(len(nums)-1):
            
            if nums[i]==nums[i+1]:
                
                nums[i]=nums[i]*2
                
                nums[i+1]=0
                
        res=[]
        
        c=[]
        
        for i in range(len(nums)):
            
            if nums[i]!=0:
                
                res.append(nums[i])
                
            else:
                
                c.append(nums[i])

        return res+c
        
                