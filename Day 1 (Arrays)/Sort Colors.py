'''
Problem Link : https://leetcode.com/problems/sort-colors/
T.C. : O(N)
S.C. : O(1)

'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high=0,0,len(nums)-1
        for i in range(len(nums)):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low=low+1
                mid=mid+1
                #print(nums)
            elif nums[mid]==1:
                mid=mid+1
                #print(nums)
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high=high-1