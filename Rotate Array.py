class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        
        arr=nums[:]
        
        for i in range(0,n):
            
            nums[i]=arr[(n-k+i)%n]
        