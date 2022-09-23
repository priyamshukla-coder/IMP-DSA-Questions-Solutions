class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        mod=int(1e9+7)
        
        res=0
        
        cnt=0
        
        for i in range(1,n+1):
            
            if i & (i-1) ==0 :
                
                cnt=cnt+1
                
            res=(res<<cnt)+i
            
            res=res%mod
            
        return res