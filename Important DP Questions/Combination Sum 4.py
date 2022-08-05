class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        def recur(a,target):
            
            if target==0:
                return 1
            
            if target<0:
                return 0
            
            cnt=0
            
            for i in range(len(a)):
                
                cnt=cnt+recur(a,target-a[i])
                
            return cnt
        
        def memoize(a,target,dp):
            
            if target==0:
                return 1
            
            if target<0:
                return 0
            
            if dp[target]!=-1:
                return dp[target]
            
            cnt=0
            
            for i in range(len(a)):
                
                cnt=cnt+memoize(a,target-a[i],dp)
            
            dp[target]=cnt
            
            return dp[target]
        
        dp=[-1 for _ in range(target+1)]
        
        def tabulate(a,target):
            
            dp=[0 for _ in range(target+1)]
            
            dp[0]=1
            
            for i in range(1,target+1):
                
                for j in range(len(a)):
                    
                    if i-a[j]>=0:
                        
                        dp[i]=dp[i]+dp[i-a[j]]
            
            return dp[target]

            #T.C. : O(m*n)
                
        return tabulate(nums,target)