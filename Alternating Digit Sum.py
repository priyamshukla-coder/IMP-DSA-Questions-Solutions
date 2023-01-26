class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        n=list(map(int,str(n)))
        
        for i in range(1,len(n),2):
            
            n[i]=n[i]*-1
            
        return sum(n)
            