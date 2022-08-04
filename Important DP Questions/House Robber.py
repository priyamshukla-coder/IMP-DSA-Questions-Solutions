class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def recur(i,a):
            
            if i==0:
                return a[i]
            
            if i<0:
                return 0
            
            pick=a[i]+recur(i-2,a)
            
            notpick=0+recur(i-1,a)
            
            return max(pick,notpick)
        
        # T.C. = O(2*n)
        # return recur(len(nums)-1,nums)
        
        def memoize(i,a,dp):
            
            if i==0:
                return a[i]
            
            if i<0:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            pick=a[i]+memoize(i-2,a,dp)
            
            notpick=0+memoize(i-1,a,dp)
            
            dp[i]=max(pick,notpick)
            
            return dp[i]
        
        # T.C.: O(N)
        # S.C. : O(N)+O(N)
        
        # dp=[-1 for _ in range(len(nums))]
        
        # return memoize(len(nums)-1,nums,dp)
        
        def tabulate(i,a):
            
            dp=[0 for _ in range(len(a))]
            
            dp[0]=a[0]
            
            neg_idx=0
            
            for idx in range(1,i):
                
                  dp[idx]=max(a[idx]+dp[idx-2],0+dp[idx-1]) if idx>1 else max(a[idx],dp[idx-1])
                    
                
            return dp[i-1]
        
        # T.C.: O(N)
        # S.C. : O(N)
        
        # return tabulate(len(nums),nums)
        
        def space_optimize(a):
            
            prev,last_prev=a[0],0
            
            for idx in range(1,len(a)):
                
                take=a[idx] if idx==1 else a[idx]+last_prev
                
                notpick=prev
                
                curr_max=max(take,notpick)
                
                last_prev=prev
                
                prev=curr_max
                
            return prev
        
        # T.C.: O(N)
        # S.C. : O(1)
        
        return space_optimize(nums)