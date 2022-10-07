class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        st=0
        
        end=len(nums)-1
        
        while st<=end:
            
            mid=(st+end)//2
            
            if nums[mid]==target:
                
                return mid
            
            elif nums[mid]<target:
                
                st=mid+1
                
            else:
                
                end=mid-1
                
        return st