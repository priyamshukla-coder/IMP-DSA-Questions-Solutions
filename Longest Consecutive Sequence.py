class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mx=0
        
        nums=set(nums)
        
        for i in nums:
            
            if i-1 not in nums:
                
                curr=i
                
                cnt=1
                
                while curr+1 in nums:
                    
                    curr=curr+1
                    
                    cnt=cnt+1
                    
                mx=max(mx,cnt)
                
        return mx
                    
                    