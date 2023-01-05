class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()

        cnt=1

        prev_point=points[0][1]

        for i in points:

            if i[0]>prev_point:

                cnt=cnt+1

                prev_point=i[1]

            prev_point=min(prev_point,i[1])

        return cnt