class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        curr_sum=0
        
        h=[-1*i for i in nums]
        
        heapq.heapify(h)
        
        while k>0:
            
            val=heapq.heappop(h)
            
            # print(val)
            
            curr_sum=curr_sum+-1*val
            
            heapq.heappush(h,-1*(-1*val+1))
            
            # print(h)
            
            k=k-1
            
        return curr_sum