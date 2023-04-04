class Solution:
    def partitionString(self, s: str) -> int:
        
        d1={}
        cnt=0
        for i in s:
            
            if i not in d1:
                d1[i]=1
            
            else:
                cnt=cnt+1
                d1={}
                d1[i]=1
        
        return cnt+1