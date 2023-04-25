class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap=[]

        for i in stones:

            heap.append(-1*i)

        heapq.heapify(heap)

        while len(heap)>=2:

            x,y=-1*heapq.heappop(heap),-1*heapq.heappop(heap)

            if x!=y:

                heapq.heappush(heap,-1*abs(x-y))

        return 0 if len(heap)==0 else -1*heapq.heappop(heap)
