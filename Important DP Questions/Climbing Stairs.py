class Solution:
    def climbStairs(self, n: int) -> int:
        
#         def recur(n):
            
#             if n==1:
#                 return 1
            
#             if n==2:
#                 return 2
            
#             return recur(n-1)+recur(n-2)
        
#         return recur(n)

# DP Approach
        if n==1: return 1

        dp=[0 for _ in range(n+1)]
    
        dp[1]=1
        dp[2]=2
        
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]



