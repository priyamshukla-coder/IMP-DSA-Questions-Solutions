class Solution:
    def minInsertions(self, s: str) -> int:

        if s==s[::-1]:

            return 0
            
        dp=[[0]*len(s) for _ in range(len(s))]

        for i in range(len(s)):

            dp[i][i]=1

        for i in range(len(s)-1,-1,-1):

            for j in range(i+1,len(s)):

                if s[i]==s[j]:

                    dp[i][j]=2+dp[i+1][j-1]

                else:

                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])

        return len(s)-dp[0][len(s)-1]