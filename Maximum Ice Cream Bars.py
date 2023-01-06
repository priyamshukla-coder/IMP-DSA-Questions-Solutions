class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        if sum(costs)<=coins:

            return len(costs)

        costs.sort()

        cnt=0

        for i in range(len(costs)):

            if coins>=costs[i]:

                coins=coins-costs[i]

                cnt=cnt+1

            else:

                break

        return cnt
        