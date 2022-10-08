class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        st=0
        
        end=len(nums)-1
        
        res=[0]*len(nums)
        
        i=len(nums)-1
        
        while i>=0:
            
            if nums[st]*nums[st]>nums[end]*nums[end]:
                
                # i=i-1
                
                res[i]=nums[st]*nums[st]
                
                st=st+1
                
            else:
                
                # i=i-1
                
                res[i]=nums[end]*nums[end]
                
                end=end-1 
            
            i=i-1
                
        return res