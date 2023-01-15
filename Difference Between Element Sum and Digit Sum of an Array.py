class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        s=sum(nums)
        
        digit_sum=0
        
        for i in nums:
            
            curr=i
            
            while curr!=0:
                
                digit_sum=digit_sum+curr%10
                
                curr=curr//10
                
        return abs(s-digit_sum)