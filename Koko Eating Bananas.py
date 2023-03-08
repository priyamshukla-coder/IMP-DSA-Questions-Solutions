class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)

        while l<r:

            mid=l+(r-l)//2

            curr=0

            for i in piles:

                curr=curr+math.ceil(i/mid)

            if curr<=h:

                r=mid

            else:

                l=mid+1

        return l