class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        nums.sort()
        
        return min(nums[len(nums)-1]-nums[2],nums[len(nums)-3]-nums[0],nums[(len(nums)-2)]-nums[1])