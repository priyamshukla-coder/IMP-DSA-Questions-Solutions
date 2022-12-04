class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        res={}
        total_sum=sum(nums)
        
        n=len(nums)
        curr_sum=0
        for i in range(n-1):
            curr_sum=curr_sum+nums[i]
            curr,left=curr_sum//(i+1),(total_sum-curr_sum)//(n-i-1)
            #print(curr,left)
            res[i]=abs(curr-left)
            #print(res)
        
        res[len(nums)-1]=sum(nums)//n
        m=min(res.values())
        
        for i in res:
            if res[i] == m:
                return i