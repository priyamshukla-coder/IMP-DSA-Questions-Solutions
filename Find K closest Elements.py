import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l1=[]
        result=[]
        for i in arr:
            val=abs(i-x)
            heapq.heappush(l1,(val,i))
        heapq.heapify(l1)
        for i in range(k):
            a=heapq.heappop(l1)
            result.append(a[1])
        result.sort()
        return result