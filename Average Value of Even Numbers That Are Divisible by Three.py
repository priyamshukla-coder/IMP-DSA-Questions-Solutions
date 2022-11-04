class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        res=[i for i in nums if i%3==0 and i%2==0]
        
        return sum(res)//len(res) if len(res)>0 else 0

