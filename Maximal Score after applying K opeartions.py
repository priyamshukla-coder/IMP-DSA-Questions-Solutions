class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        h=[]
        
        for i in nums:
            
            heapq.heappush(h,-1*i)
    
        score=0
        
        while k!=0:
            
            val=-1*heapq.heappop(h)
            
            score=score+val
            
            heapq.heappush(h,-1*math.ceil(val/3))
            
            k=k-1
            
        return score
            