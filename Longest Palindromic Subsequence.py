class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        dp=[[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]

        reverse=s[::-1]

        for i in range(len(s)-1,-1,-1):

            for j in range(len(s)-1,-1,-1):

                dp[i][j]=1+dp[i+1][j+1] if s[i]==reverse[j] else max(dp[i+1][j],dp[i][j+1])


        return dp[0][0]
                    