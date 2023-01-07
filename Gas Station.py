class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):

            return -1

        total,pos=0,0

        for i in range(len(gas)):

            total=total+gas[i]-cost[i]

            if total<0:

                pos=i+1

                total=0

        return pos