class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        
        res=[]
        
        for i in queries:
            
            st=0
            
            curr_sum=0
            
            while st<len(nums) and curr_sum+nums[st]<=i:
                
                curr_sum=curr_sum+nums[st]
                
                # print(curr_sum)
                
                st=st+1
                
            res.append(st)
            
        return res