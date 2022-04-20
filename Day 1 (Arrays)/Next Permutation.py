'''
Problem Link : https://leetcode.com/problems/next-permutation/
Date : 15/04/2022
T.C. : O(N)
S.C. : O(1)

'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        idx=-1
        i=l-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        print(i)
        
        if i<0:
            nums.reverse()
        else:
        
            for j in range(l-1,i,-1):
                if nums[j]>nums[i]:
                    break
            print(j)

            nums[j],nums[i]=nums[i],nums[j]
            print(nums)

            st=i+1
            end=l-1
            while st<end:
                nums[st],nums[end]=nums[end],nums[st]
                st=st+1
                end=end-1
        
    