class SmallestInfiniteSet:

    def __init__(self):

        self.val=1

        self.heap=[]

        heap=[i for i in range(1,1001)]

        heapq.heapify(self.heap)
        

    def popSmallest(self) -> int:

        if len(self.heap)>0:

            return heapq.heappop(self.heap)

        curr=self.val

        self.val=self.val+1

        return curr
        

    def addBack(self, num: int) -> None:

        if num>=self.val:

            return 

        if num in self.heap:

            return 
        
        heapq.heappush(self.heap,num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)