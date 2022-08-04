'''
Problem Link : https://leetcode.com/problems/maximum-subarray/
T.C. : O(N)
S.C. : O(1)

'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum=0
        max_sum=float("-inf")
        for i in range(len(nums)):
            curr_sum=curr_sum+nums[i]
            
            if curr_sum>max_sum:
                max_sum=curr_sum
                
            if curr_sum<0:
                curr_sum=0
                
            
        return max_sum