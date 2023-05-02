class Solution:
    def average(self, salary: List[int]) -> float:

        mx,mn=max(salary),min(salary)

        curr=0

        cnt=0

        for i in salary:

            if i==mx or i==mn:

                continue

            else:
                # print(i)

                curr=curr+i

                cnt=cnt+1

        return curr/cnt