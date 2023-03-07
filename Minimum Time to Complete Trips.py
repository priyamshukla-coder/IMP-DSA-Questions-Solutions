class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        l,r=0,min(time)*totalTrips

        while l<r:

            mid=l+(r-l)//2

            curr=0

            for i in time:

                curr=curr+mid//i

            if curr>=totalTrips:

                r=mid

            else:

                l=mid+1

            curr=0

        return l