class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        
        xor=nums[0]
        
        for i in nums[1:]:
            
            xor=xor^i
            
        return xor