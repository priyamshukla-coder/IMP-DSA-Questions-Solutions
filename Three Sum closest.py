class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m1=float("inf")
        nums.sort()
        if len(nums)<3:
            return 
        for i in range(len(nums)-2):
            start,end=i+1,len(nums)-1
            while start<end:
                val=nums[i]+nums[start]+nums[end]
                if abs(val-target)==0:
                    return val
                elif abs(val-target)<m1:
                    m1=abs(val-target)
                    diff=val
                if (val-target)>0:
                    end=end-1
                else:
                    start=start+1
        return diff