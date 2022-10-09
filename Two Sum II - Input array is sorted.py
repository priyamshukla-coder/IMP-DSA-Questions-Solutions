class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        d1={}
        
        nums=numbers
        
        for i in range(len(nums)):
            
            diff=target-nums[i]
            
            if diff in d1:
                
                return [d1[diff]+1,i+1]
                
                
            d1[nums[i]]=i
            
            