class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d1={}
        
        for i in range(len(nums)):
            
            if nums[i] not in d1:
                
                d1[nums[i]]=i
                
            else:
                
                if abs(i-d1[nums[i]])<=k:
                    
                    return True
                
                d1[nums[i]]=i
                
        return False
                
            