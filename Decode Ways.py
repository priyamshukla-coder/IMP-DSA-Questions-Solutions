class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp=[-1]*len(s)
        
        def d(st,s,dp):
            
            if st==len(s):
                
                return 1
            
            if dp[st]!=-1:
                
                return dp[st]
            
            if s[st]=='0':
                
                return 0
            
            val=d(st+1,s,dp)
            
            if st<len(s)-1 and (s[st]=='1' or s[st]=='2' and s[st+1]<'7'):
                
                val=val+d(st+2,s,dp)
                
            dp[st]=val
            
            return dp[st]
        
        return d(0,s,dp)
        
                