class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        mx=max(nums)
        
        res=[i for i in range(1,mx)]
        
        res.append(mx)
        
        res.append(mx)
        
        c=Counter(nums)
        
        cnt_res=Counter(res)
        
        return True if c==cnt_res else False