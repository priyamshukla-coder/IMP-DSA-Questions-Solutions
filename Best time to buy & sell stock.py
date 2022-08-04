'''
Problem Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
T.C. : O(N)
S.C. : O(1)

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_amt=prices[0]
        max_profit=0
        for i in range(len(prices)):
            min_amt=min(min_amt,prices[i])
            max_profit=max(max_profit,prices[i]-min_amt)
        return max_profit