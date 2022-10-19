class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        c=Counter(words)
        
        h=[]
        
        for i in c:
            
            heapq.heappush(h,[-1*c[i],i])
            
        # heapq.heapify(h)
            
        res=[]
        
        while k!=0:
            
            res.append(heapq.heappop(h)[1])
            
            k=k-1
            
        return res