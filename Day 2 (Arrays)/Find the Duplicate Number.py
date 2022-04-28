'''
Problem Link : https://leetcode.com/problems/find-the-duplicate-number/
T.C. : O(N)
S.C. : O(1)

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=nums[0],nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break
        
        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        print(slow,fast)
        return fast