class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        cnt,curr_zero_subarrays=0,0

        for i in range(len(nums)):

            if nums[i]==0:

                curr_zero_subarrays+=1

            elif nums[i]:

                curr_zero_subarrays=0

            cnt=cnt+curr_zero_subarrays

        return cnt
