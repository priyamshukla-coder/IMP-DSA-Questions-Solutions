class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if nums.count(0) == len(nums):
            return 0
        
        return len(set(nums))-list(set(nums)).count(0)
        
        
