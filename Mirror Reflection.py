class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        while p%2==0 and q%2==0:
            p=p//2
            q=q//2
            
        val=p%2-q%2
        
        return 1-val