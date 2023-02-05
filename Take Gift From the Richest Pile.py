class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        h=[]
        
        for i in gifts:
            
            h.append(-1*i)
            
        heapq.heapify(h)
        
        while k!=0:
            
            val=-1*heapq.heappop(h)
            
            rem=math.sqrt(val)
            
            heapq.heappush(h,-1*int(rem))
            
            k=k-1
            
        return -1*sum(h)

