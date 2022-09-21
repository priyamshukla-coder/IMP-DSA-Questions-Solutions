class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ev=0
        
        for i in nums:
            
            if i%2==0:
                
                ev=ev+i
                
        res=[]
        
        for i in range(len(queries)):
            
            val,idx=queries[i][0],queries[i][1]
            
            if nums[idx] % 2 == 0:
                
                ev=ev-nums[idx]
                
            nums[idx]=nums[idx]+val
                
            if nums[idx] % 2 == 0:
                
                ev=ev+nums[idx]
                
            res.append(ev)
            
        return res